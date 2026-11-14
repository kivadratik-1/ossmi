# How to install and run the OSSMI scripts in Autodesk Fusion

Two scripts:

- **OSSMI Host Plate** (`ossmi_host`): host plate with underside cavity, clutch tubes and through-holes.
- **OSSMI Adapter Plate** (`ossmi_adapter`): mating plate with a grid of studs.

Source: https://github.com/kivadratik-1/ossmi

## Folder layout

Each script is a folder. The folder, the `.py` file and the `.manifest` file must share the same name:


## Install

**Option A: link the folder (any location)**

1. In Fusion, open **UTILITIES > Add-Ins > Scripts and Add-Ins**.
2. Click **+** and choose **Script or add-in from device**.
3. Select the script folder (e.g. `ossmi_host`). Fusion remembers it and adds it to the list.

**Option B: copy to the default Scripts folder**

Copy the whole script folder to:

- Windows: `%appdata%\Autodesk\Autodesk Fusion 360\API\Scripts`
- macOS: `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts`

Then restart Fusion.

## Run

1. Create or open a **new empty design** (the plate is added to the active document).
2. Open **UTILITIES > Add-Ins > Scripts and Add-Ins**.
3. On the **Scripts** tab, select the script and click **Run**.
4. Set the parameters in the dialog (all sizes in mm) and click **OK**.

The body is created and named with its parameters, for example:

- `ossmi-base_6x4_1.5_6.51_4.4_0.20`
- `ossmi-adapter_8x5_0.8_4.8_1.8_0.20`

## Notes

- Running a script again adds another body to the same document. Use a clean document for each plate.
- If a script does not appear in the list, check that the folder, `.py` and `.manifest` names match, and that the `.manifest` is valid JSON.
- Geometry is experimental. Test the physical fit before relying on it.

