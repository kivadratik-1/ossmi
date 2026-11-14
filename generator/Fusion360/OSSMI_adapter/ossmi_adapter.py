import adsk.core, adsk.fusion, traceback

CMD_ID = 'ossmiAdapterPlateCmd'
PITCH = 0.8    # cm (8 mm)

_handlers = []


# ---------- Geometry helpers ----------

def add_rect(sketch, x0, y0, x1, y1):
    sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        adsk.core.Point3D.create(x0, y0, 0),
        adsk.core.Point3D.create(x1, y1, 0))


def add_circle(sketch, cx, cy, d):
    sketch.sketchCurves.sketchCircles.addByCenterRadius(
        adsk.core.Point3D.create(cx, cy, 0), d / 2)


def extrude(comp, sketch, distance, op):
    profiles = adsk.core.ObjectCollection.create()
    for p in sketch.profiles:
        profiles.add(p)
    ext = comp.features.extrudeFeatures
    inp = ext.createInput(profiles, op)
    inp.setDistanceExtent(False, adsk.core.ValueInput.createByReal(distance))
    return ext.add(inp)


# ---------- Parameters and name ----------

def read_params(inputs):
    """Reads values from the dialog. Lengths are returned in cm."""
    return dict(
        nx=inputs.itemById('nx').value,
        ny=inputs.itemById('ny').value,
        base=inputs.itemById('base').value,
        stud_d=inputs.itemById('stud_d').value,
        stud_h=inputs.itemById('stud_h').value,
        edge=inputs.itemById('edge').value,
    )


def check_params(p):
    """Returns an error text or None if parameters are valid."""
    if min(p['base'], p['stud_d'], p['stud_h']) <= 0:
        return 'Values for base, stud_d, and stud_h must be greater than 0.'
    if p['edge'] < 0:
        return 'Edge reduction cannot be negative.'
    if p['stud_d'] > PITCH - p['edge']:
        return 'The stud diameter is too large: it extends beyond the plate edge.'
    return None


def fmt_mm(v_cm):
    """cm -> mm without unnecessary zeros: 0.08 -> '0.8'."""
    return f'{round(v_cm * 10, 4):g}'


def make_name(p):
    return (f"ossmi-adapter_{p['nx']}x{p['ny']}"
            f"_{fmt_mm(p['base'])}"
            f"_{fmt_mm(p['stud_d'])}"
            f"_{fmt_mm(p['stud_h'])}"
            f"_{p['edge'] * 10:.2f}")


# ---------- Construction ----------

def build_plate(p):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    nx, ny = p['nx'], p['ny']
    width = nx * PITCH - p['edge']
    length = ny * PITCH - p['edge']
    inset = (PITCH - p['edge']) / 2
    total_h = p['base'] + p['stud_h']
    F = adsk.fusion.FeatureOperations

    bodies_before = root.bRepBodies.count

    # 1. Rectangular base, lower face at Z=0
    sk = root.sketches.add(root.xYConstructionPlane)
    add_rect(sk, 0, 0, width, length)
    extrude(root, sk, p['base'], F.NewBodyFeatureOperation)

    # The new body is added to the end of the list: assign the name immediately
    body = root.bRepBodies.item(bodies_before)
    body.name = make_name(p)

    # 2. Studs: circles at Z=0 are extruded to base + stud_h
    #    and joined to the base. The portion inside the base merges with it,
    #    so the result is the same as studs placed on the top face.
    sk2 = root.sketches.add(root.xYConstructionPlane)
    for ix in range(nx):
        for iy in range(ny):
            add_circle(sk2, inset + ix * PITCH, inset + iy * PITCH, p['stud_d'])
    extrude(root, sk2, total_h, F.JoinFeatureOperation)

    app.activeViewport.fit()
    return width, length, total_h


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
            width, length, total_h = build_plate(p)
            ui.messageBox(f"Created body {make_name(p)}\n"
                          f"{width * 10:g} x {length * 10:g} x {total_h * 10:g} mm, "
                          f"studs: {p['nx'] * p['ny']}")
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
            # Values are in cm internally; the dialog displays them in mm
            inputs.addValueInput('base', 'base thickness', 'mm', VI.createByReal(0.08))
            inputs.addValueInput('stud_d', 'stud diameter', 'mm', VI.createByReal(0.48))
            inputs.addValueInput('stud_h', 'stud height', 'mm', VI.createByReal(0.18))
            inputs.addValueInput('edge', 'edge reduction', 'mm', VI.createByReal(0.02))

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
            CMD_ID, 'OSSMI Adapter Plate', 'OSSMI adapter plate generator with studs')

        onCreated = CreatedHandler()
        cmdDef.commandCreated.add(onCreated)
        _handlers.append(onCreated)

        cmdDef.execute()
        adsk.autoTerminate(False)  # keeps the script active while the dialog is open
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
