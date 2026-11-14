import adsk.core, adsk.fusion, traceback

CMD_ID = 'ossmiAdapterPlateCmd'

# Dimensions are kept in millimeters throughout the script.
PITCH = 8.0
BASE_THICKNESS = 0.8
STUD_OUTER_DIAMETER = 4.8
STUD_INNER_DIAMETER = 3.3
STUD_HEIGHT = 1.8
EDGE_REDUCTION = 0.2
CHAMFER_SIZE = 0.2
TOLERANCE = 1e-4

_handlers = []


# ---------- Geometry helpers ----------

def add_rect(sketch, x0, y0, x1, y1):
    sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        adsk.core.Point3D.create(x0, y0, 0),
        adsk.core.Point3D.create(x1, y1, 0))


def add_circle(sketch, cx, cy, d):
    sketch.sketchCurves.sketchCircles.addByCenterRadius(
        adsk.core.Point3D.create(cx, cy, 0), d / 2)


def extrude_profiles(comp, profiles, distance, op):
    """Extrudes the specified profile collection."""
    ext = comp.features.extrudeFeatures
    inp = ext.createInput(profiles, op)
    inp.setDistanceExtent(False, adsk.core.ValueInput.createByReal(distance))
    return ext.add(inp)


def extrude(comp, sketch, distance, op):
    """Extrudes all profile curves from the sketch."""
    profiles = adsk.core.ObjectCollection.create()
    for p in sketch.profiles:
        profiles.add(p)
    return extrude_profiles(comp, profiles, distance, op)


# ---------- Parameters and name ----------

def read_params(inputs):
    """Reads values from the dialog. All lengths are stored in millimeters."""
    return dict(
        nx=inputs.itemById('nx').value,
        ny=inputs.itemById('ny').value,
        base=inputs.itemById('base').value,
        stud_outer_diameter=inputs.itemById('stud_d').value,
        stud_inner_diameter=inputs.itemById('stud_id').value,
        stud_height=inputs.itemById('stud_h').value,
        edge_reduction=inputs.itemById('edge').value,
        through=inputs.itemById('through').value,
        chamfer=inputs.itemById('chamfer').value,
        chamfer_size=inputs.itemById('chamfer_d').value,
    )


def check_params(p):
    """Returns an error text or None if parameters are valid."""
    if min(p['base'], p['stud_outer_diameter'], p['stud_inner_diameter'], p['stud_height']) <= 0:
        return 'Values for base, stud_outer_diameter, stud_inner_diameter, and stud_height must be greater than 0.'
    if p['edge_reduction'] < 0:
        return 'Edge reduction cannot be negative.'
    if p['stud_inner_diameter'] >= p['stud_outer_diameter']:
        return 'The stud inner diameter must be smaller than the outer diameter.'
    if p['stud_outer_diameter'] > PITCH - p['edge_reduction']:
        return 'The stud diameter is too large: it extends beyond the plate edge.'
    if p['chamfer']:
        if p['chamfer_size'] <= 0:
            return 'The chamfer size must be greater than 0.'
        if p['chamfer_size'] >= (p['stud_outer_diameter'] - p['stud_inner_diameter']) / 2:
            return 'The chamfer must be smaller than the stud wall thickness.'
        if p['chamfer_size'] >= p['stud_height']:
            return 'The chamfer must be smaller than the stud height.'
    return None


def fmt_mm(v_mm):
    """Format a distance in mm without unnecessary zeros."""
    return f'{round(v_mm, 4):g}'


def make_name(p):
    name = (f"ossmi-adapter_{p['nx']}x{p['ny']}"
            f"_{fmt_mm(p['base'])}"
            f"_{fmt_mm(p['stud_outer_diameter'])}"
            f"_{fmt_mm(p['stud_inner_diameter'])}"
            f"_{fmt_mm(p['stud_height'])}"
            f"_{p['edge_reduction']:.2f}")
    if p['through']:
        name += '_thru'
    if p['chamfer']:
        name += f"_ch{fmt_mm(p['chamfer_size'])}"
    return name


# ---------- Construction ----------

def find_stud_top_edges(body, stud_outer_diameter, top_z):
    """Outer end edges of the studs: circles of diameter stud_outer_diameter at height top_z."""
    edges = adsk.core.ObjectCollection.create()
    for e in body.edges:
        g = e.geometry
        if g.objectType != 'adsk::core::Circle3D':
            continue
        if abs(g.radius - stud_outer_diameter / 2) < TOLERANCE and abs(g.center.z - top_z) < TOLERANCE:
            edges.add(e)
    return edges


def build_plate(p):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    nx, ny = p['nx'], p['ny']
    width = nx * PITCH - p['edge_reduction']
    length = ny * PITCH - p['edge_reduction']
    inset = (PITCH - p['edge_reduction']) / 2
    total_height = p['base'] + p['stud_height']
    F = adsk.fusion.FeatureOperations

    bodies_before = root.bRepBodies.count

    # 1. Rectangular base, lower face at Z=0
    sk = root.sketches.add(root.xYConstructionPlane)
    add_rect(sk, 0, 0, width, length)
    extrude(root, sk, p['base'], F.NewBodyFeatureOperation)

    # The new body is added to the end of the list: assign the name immediately
    body = root.bRepBodies.item(bodies_before)
    body.name = make_name(p)

    # 2. Tubular studs: only ring profiles are extruded
    sk2 = root.sketches.add(root.xYConstructionPlane)
    for ix in range(nx):
        for iy in range(ny):
            cx = inset + ix * PITCH
            cy = inset + iy * PITCH
            add_circle(sk2, cx, cy, p['stud_outer_diameter'])
            add_circle(sk2, cx, cy, p['stud_inner_diameter'])

    rings = adsk.core.ObjectCollection.create()
    for prof in sk2.profiles:
        if prof.profileLoops.count == 2:
            rings.add(prof)
    extrude_profiles(root, rings, total_height, F.JoinFeatureOperation)

    # 3. Optional: through hole in the base
    if p['through']:
        sk3 = root.sketches.add(root.xYConstructionPlane)
        for ix in range(nx):
            for iy in range(ny):
                add_circle(sk3, inset + ix * PITCH, inset + iy * PITCH, p['stud_inner_diameter'])
        extrude(root, sk3, total_height, F.CutFeatureOperation)

    # 4. Optional: 45° chamfer on the outer top edge of each stud
    chamfered = 0
    if p['chamfer']:
        body = root.bRepBodies.item(bodies_before)  # fresh body reference
        edges = find_stud_top_edges(body, p['stud_outer_diameter'], total_height)
        chamfered = edges.count
        if chamfered:
            chamfers = root.features.chamferFeatures
            cin = chamfers.createInput2()
            cin.chamferEdgeSets.addEqualDistanceChamferEdgeSet(
                edges, adsk.core.ValueInput.createByReal(p['chamfer_size']), False)
            chamfers.add(cin)

    app.activeViewport.fit()
    return width, length, total_height, chamfered


# ---------- Dialog handlers ----------

class ValidateHandler(adsk.core.ValidateInputsEventHandler):
    def notify(self, args):
        try:
            args = adsk.core.ValidateInputsEventArgs.cast(args)
            p = read_params(args.inputs)
            args.areInputsValid = check_params(p) is None
        except:
            args.areInputsValid = False


class ExecuteHandler(adsk.core.CommandEventHandler):
    def notify(self, args):
        ui = adsk.core.Application.get().userInterface
        try:
            cmd = adsk.core.Command.cast(args.firingEvent.sender)
            p = read_params(cmd.commandInputs)
            err = check_params(p)
            if err:
                ui.messageBox(err)
                return
            width, length, total_height, chamfered = build_plate(p)
            msg = (f"Created body {make_name(p)}\n"
                   f"{width:g} x {length:g} x {total_height:g} mm, "
                   f"tubular studs: {p['nx'] * p['ny']}")
            if p['chamfer']:
                msg += f"\nChamfered edges: {chamfered} of {p['nx'] * p['ny']}"
            ui.messageBox(msg)
        except:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


class DestroyHandler(adsk.core.CommandEventHandler):
    def notify(self, args):
        adsk.terminate()


class CreatedHandler(adsk.core.CommandCreatedEventHandler):
    def notify(self, args):
        ui = adsk.core.Application.get().userInterface
        try:
            cmd = adsk.core.Command.cast(args.command)
            inputs = cmd.commandInputs
            VI = adsk.core.ValueInput

            inputs.addIntegerSpinnerCommandInput('nx', 'nx (studs along X)', 1, 100, 1, 8)
            inputs.addIntegerSpinnerCommandInput('ny', 'ny (studs along Y)', 1, 100, 1, 5)
            inputs.addValueInput('base', 'base thickness', 'mm', VI.createByReal(BASE_THICKNESS))
            inputs.addValueInput('stud_d', 'stud outer diameter', 'mm', VI.createByReal(STUD_OUTER_DIAMETER))
            inputs.addValueInput('stud_id', 'stud inner diameter', 'mm', VI.createByReal(STUD_INNER_DIAMETER))
            inputs.addValueInput('stud_h', 'stud height', 'mm', VI.createByReal(STUD_HEIGHT))
            inputs.addValueInput('edge', 'edge reduction', 'mm', VI.createByReal(EDGE_REDUCTION))
            inputs.addBoolValueInput('through', 'bore through base too', True, '', False)
            inputs.addBoolValueInput('chamfer', 'chamfer stud top outer edge', True, '', True)
            inputs.addValueInput('chamfer_d', 'chamfer size (45°)', 'mm', VI.createByReal(CHAMFER_SIZE))

            onValidate = ValidateHandler()
            cmd.validateInputs.add(onValidate)
            _handlers.append(onValidate)

            onExecute = ExecuteHandler()
            cmd.execute.add(onExecute)
            _handlers.append(onExecute)

            onDestroy = DestroyHandler()
            cmd.destroy.add(onDestroy)
            _handlers.append(onDestroy)
        except:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


# ---------- Entry point ----------

def run(_context: str):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        cmdDef = ui.commandDefinitions.itemById(CMD_ID)
        if cmdDef:
            cmdDef.deleteMe()
        cmdDef = ui.commandDefinitions.addButtonDefinition(
            CMD_ID, 'OSSMI Adapter Plate', 'OSSMI adapter plate generator with tubular studs')

        onCreated = CreatedHandler()
        cmdDef.commandCreated.add(onCreated)
        _handlers.append(onCreated)

        cmdDef.execute()
        adsk.autoTerminate(False)  # keeps the script active while the dialog is open
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
