import adsk.core, adsk.fusion, traceback

CMD_ID = 'ossmiHostPlateCmd'
PITCH = 0.8    # cm (8 mm)
HEIGHT = 0.3   # cm (3 mm)

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

def read_parameters(inputs):
    """Reads values from the dialog. Lengths are returned in cm."""
    return dict(
        columns=inputs.itemById('nx').value,
        rows=inputs.itemById('ny').value,
        skin=inputs.itemById('skin').value,
        wall=inputs.itemById('wall').value,
        tube_outer_diameter=inputs.itemById('tube_od').value,
        tube_inner_diameter=inputs.itemById('tube_id').value,
        allowance=inputs.itemById('allowance').value,
    )


def validate_parameters(p):
    """Returns an error text or None if parameters are valid."""
    plate_width = p['columns'] * PITCH - p['allowance']
    plate_length = p['rows'] * PITCH - p['allowance']
    if min(p['skin'], p['wall'], p['tube_outer_diameter'], p['tube_inner_diameter']) <= 0:
        return 'Values for skin, wall, tube_od, and tube_id must be greater than 0.'
    if p['allowance'] < 0:
        return 'Edge allowance cannot be negative.'
    if p['skin'] >= HEIGHT:
        return 'Skin must be less than the plate height (3 mm).'
    if p['tube_inner_diameter'] >= p['tube_outer_diameter']:
        return 'tube_id must be smaller than tube_od.'
    if p['tube_outer_diameter'] >= PITCH:
        return 'tube_od must be smaller than the pitch (8 mm).'
    if 2 * p['wall'] >= min(plate_width, plate_length):
        return 'The wall is too thick for this plate size.'
    return None


def format_mm(value_cm):
    """cm -> mm without unnecessary zeros: 0.15 -> '1.5'."""
    return f'{round(value_cm * 10, 4):g}'


def generate_body_name(p):
    return (f"ossmi-base_{p['columns']}x{p['rows']}"
            f"_{format_mm(p['wall'])}"
            f"_{format_mm(p['tube_outer_diameter'])}"
            f"_{format_mm(p['tube_inner_diameter'])}"
            f"_{p['allowance'] * 10:.2f}")


# ---------- Construction ----------

def build_plate(p):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    root = design.rootComponent
    columns, rows = p['columns'], p['rows']
    width = columns * PITCH - p['allowance']
    length = rows * PITCH - p['allowance']
    offset = p['allowance'] / 2
    feature_ops = adsk.fusion.FeatureOperations

    bodies_before = root.bRepBodies.count

    # 1. Outer body
    sketch = root.sketches.add(root.xYConstructionPlane)
    add_rect(sketch, 0, 0, width, length)
    extrude(root, sketch, HEIGHT, feature_ops.NewBodyFeatureOperation)

    # The new body is added to the end of the list: assign the name immediately
    body = root.bRepBodies.item(bodies_before)
    body.name = generate_body_name(p)

    # 2. Bottom cavity
    cavity_sketch = root.sketches.add(root.xYConstructionPlane)
    add_rect(cavity_sketch, p['wall'], p['wall'], width - p['wall'], length - p['wall'])
    extrude(root, cavity_sketch, HEIGHT - p['skin'], feature_ops.CutFeatureOperation)

    # 3. Tubes under the posts (only if there are internal positions)
    if columns > 1 and rows > 1:
        tube_sketch = root.sketches.add(root.xYConstructionPlane)
        for x_index in range(1, columns):
            for y_index in range(1, rows):
                add_circle(tube_sketch, x_index * PITCH - offset, y_index * PITCH - offset, p['tube_outer_diameter'])
        extrude(root, tube_sketch, HEIGHT - p['skin'], feature_ops.JoinFeatureOperation)

        # 4. Through holes
        hole_sketch = root.sketches.add(root.xYConstructionPlane)
        for x_index in range(1, columns):
            for y_index in range(1, rows):
                add_circle(hole_sketch, x_index * PITCH - offset, y_index * PITCH - offset, p['tube_inner_diameter'])
        extrude(root, hole_sketch, HEIGHT, feature_ops.CutFeatureOperation)

    app.activeViewport.fit()
    return width, length


# ---------- Dialog handlers ----------

class ValidateHandler(adsk.core.ValidateInputsEventHandler):
    def notify(self, args):
        try:
            args = adsk.core.ValidateInputsEventArgs.cast(args)
            p = read_parameters(args.inputs)
            args.areInputsValid = validate_parameters(p) is None
        except:
            args.areInputsValid = False


class ExecuteHandler(adsk.core.CommandEventHandler):
    def notify(self, args):
        ui = adsk.core.Application.get().userInterface
        try:
            cmd = adsk.core.Command.cast(args.firingEvent.sender)
            p = read_parameters(cmd.commandInputs)
            err = validate_parameters(p)
            if err:
                ui.messageBox(err)
                return
            width, length = build_plate(p)
            ui.messageBox(f"Created body {generate_body_name(p)}\n"
                          f"{width * 10:g} x {length * 10:g} x {HEIGHT * 10:g} mm")
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

            inputs.addIntegerSpinnerCommandInput('nx', 'nx (positions along X)', 1, 100, 1, 4)
            inputs.addIntegerSpinnerCommandInput('ny', 'ny (positions along Y)', 1, 100, 1, 4)
            # Values are in cm internally; the dialog displays them in mm
            inputs.addValueInput('skin', 'skin (top wall)', 'mm', VI.createByReal(0.1))
            inputs.addValueInput('wall', 'wall (side wall)', 'mm', VI.createByReal(0.15))
            inputs.addValueInput('tube_od', 'tube_od', 'mm', VI.createByReal(0.651))
            inputs.addValueInput('tube_id', 'tube_id', 'mm', VI.createByReal(0.44))
            inputs.addValueInput('allowance', 'edge allowance', 'mm', VI.createByReal(0.02))

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
            CMD_ID, 'OSSMI Host Plate', 'OSSMI plate generator')

        onCreated = CreatedHandler()
        cmdDef.commandCreated.add(onCreated)
        _handlers.append(onCreated)

        cmdDef.execute()
        adsk.autoTerminate(False)  # keeps the script active while the dialog is open
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
