# OSSMI-S — FDM Heat-Set Insert and Grid Calibration

**Status:** Experimental maker procedure / draft for community validation  
**Scope:** FDM-printed OSSMI-S receiving pads with M3 heat-set threaded inserts  
**Related guide:** [FDM fit calibration using ordinary LEGO parts](FDM_CALIBRATION.md)

## 1. Purpose and acceptance principle

The OSSMI-S process must preserve three properties *in the finished, cooled part*:

1. The ordinary LEGO System reference part still engages with the OSSMI receiving geometry with a repeatable, secure, removable friction fit.
2. The M3 threaded insert centers remain on the **8.0 mm nominal orthogonal grid**.
3. M3 screws engage normally without binding, severe tilt, cracked plastic or insert rotation.

A part that passes fit checks **before** heat-setting but fails **after** heat-setting does **not** pass OSSMI-S calibration. Heat-setting can distort the outside of a receiving tube and shift or tilt its insert. Neither correct CAD dimensions nor a good initial LEGO fit alone establish a pass.

The ordinary functional fit reference is **any undamaged, unmodified, genuine, mass-produced LEGO System construction-set element with a compatible mating shape**. It is not a special calibration brick or metrological gauge. Use the **same physical LEGO piece** in before/after tests to make comparisons meaningful. LEGO fit does not establish the insert grid accuracy; caliper measurements serve that separate purpose.

## 2. Fixed versus adjustable generator parameters

| Feature | Generator policy | Initial experimental values |
|---|---|---|
| X/Y center pitch of the OSSMI grid | **FIXED — never adjustable** | **8.00 mm** |
| Outside diameter of receiving tube / skirt | Adjustable for physical LEGO fit | Nominal **6.50 mm**; trial sweep **6.30–6.80 mm** |
| Bore / heat-set insert pilot diameter | Adjustable to actual insert and plastic | Nominal **4.80 mm** in the current prototype; trial sweep **4.30–5.00 mm** |
| Grid-to-plate-edge margin / outline | Adjustable within structural limits | No universal range assigned |

These diameter ranges are **starting points for experiments**, not standardized tolerances or a guarantee of safety. A particular insert may require a pilot diameter *outside* the trial range; use the insert manufacturer's installation advice when available. Do not assume that all inserts sold as “M3” have the same outside diameter, length, knurl profile or recommended pilot bore.

**Important geometric distinction:** the existing prototype's 4.8 mm through-bore is not necessarily a safe or correct heat-set pilot for every M3 insert. If the pilot hole and open through-channel share geometry, examine whether sufficient plastic remains in the surrounding tube and whether insertion bulges its outer wall. The generator should identify these as separate parameters whenever the actual design uses separate features. Adjusting a tube outer diameter or insert pilot must **never silently alter the 8 mm center pitch**. Changing the plate edge margin moves the outline relative to the grid; it must not change grid spacing.

## 3. Basic tools and specimen

- A digital or vernier caliper, preferably with usable outside and inside jaws.
- The intended 3D printer, filament, slicer settings and orientation.
- The exact M3 heat-set inserts to be used, a matching soldering-iron tip or insertion tool, and two equal M3 screws for optional alignment checks.
- An ordinary compatible genuine LEGO construction-set piece; a second piece is useful for independent confirmation.
- A flat, heat-tolerant surface and a means to hold the part steady, without crushing it.

Print a **2×5 or larger grid** where practical, with both X and Y directions represented (for example, 5×5), so that both a single **8 mm** pitch and a four-interval **32 mm** baseline can be checked along *each* axis. Include the actual receiving tubes and their insert bores, not abstract test holes with different wall geometry. Use the same layer height, material, orientation and print settings intended for final parts.

## 4. Calibration sequence

### Stage A — initial print and pre-insertion fit

1. Fix the 8 mm grid pitch in the generator. Select a skirt outside diameter and pilot-hole diameter. Record both values and the edge margin.
2. Print the coupon and allow it to cool. Remove only loose strings, brims and unwanted supports. **Do not sand, drill or heat-form mating surfaces** before the initial test.
3. Test the receiving interface against a compatible ordinary LEGO brick or plate. Join straight by hand, observe full seating and noticeable play, and remove without damage. Repeat five times. Record **PASS**, **TOO TIGHT**, **TOO LOOSE**, or **INCONSISTENT**.
4. Measure the outside diameter of several receiving tubes in two directions when accessible; record the observations. These are diagnostic values, not substitutes for functional fit.
5. Measure the unheated insert-hole geometry and, where accessible, initial grid baselines using the method in Section 6.

If the unheated LEGO fit is unacceptable, adjust the skirt diameter or relevant print compensation **without changing center pitch**, reprint and repeat Stage A.

### Stage B — install M3 inserts

1. Follow the actual insert maker's temperature and hole guidance where available. A soldering iron setpoint is **not** a validated universal temperature for all insert/filament combinations.
2. Keep the insert coaxial to its printed hole and advance it without lateral force. Avoid pressing so hard or heating so long that the tube bulges or neighboring elements move.
3. Seat the insert at the intended depth; ensure it does not protrude into a LEGO mating surface or block the screw path.
4. Allow the entire coupon to cool to room temperature **without load or fit testing while soft**.
5. Inspect visually for cracks, bulging, sink marks, out-of-square inserts and local distortion.

### Stage C — mandatory post-insertion calibration

1. Measure the same tubes again at the same accessible positions and directions. For each: **ΔD = outside diameter after − outside diameter before**. Record a visible bulge or out-of-roundness even if a single caliper reading appears acceptable.
2. Repeat the full five-cycle fit test using **the same LEGO reference piece**. The LEGO must still seat with normal hand pressure, retain without obvious wobble or accidental release under light handling, and detach manually without damage. Heat-setting may make the fit *tighter or looser*.
3. Measure the M3 insert grid along both X and Y: adjacent nominal center distance **8 mm**, and first-to-fifth center distance **32 mm**. Use Section 6 and record the actual readings, not just “looks aligned.”
4. Start an M3 screw in every tested insert **with fingers only**: check easy engagement, absence of cross-threading and obvious angular misalignment. Check that the insert does not spin under gentle hand installation. Do not use maximum torque as a fit test.
5. If possible, mount an appropriately drilled mating coupon using **two separated screws**. Both must start by hand without having to force a screw sideways; this is a valuable functional cross-check for accumulated pitch error and tilt.

**Final acceptance is based on the cooled, insert-installed part.** A good Stage A result does not excuse failure at Stage C.

## 5. What the 8 mm grid measurement actually checks

For centers along the same axis:

- Adjacent elements: **8.00 mm nominal** (one interval).
- First through fifth elements: **32.00 mm nominal** (four intervals).
- Repeat in **X and Y**. The longer baseline exposes scale error which may be hard to see over a single 8 mm interval.

When possible, inspect a rectangular arrangement for skew by comparing its two diagonals. For a rectangle spanning four 8 mm intervals in X and four in Y, the nominal diagonal is **√(32² + 32²) ≈ 45.25 mm**. Equal diagonals alone cannot prove squareness or exact pitch; treat them as diagnostic evidence alongside axial measurements and fit tests.

There is **no finalized OSSMI-S pass/fail dimensional tolerance** in this draft. A proposed **±0.10 mm over 32 mm** is only an *experimental target*, pending cross-printer measurements and real multi-screw assemblies. Do not label it a certified standard tolerance.

## 6. Measuring center distance with a standard caliper

### Method A — two cylindrical holes or insert rims

For two accessible, nearly circular openings, measure their **nearest-edge gap** `G` and their **outermost-edge span** `O`, on the same axis. The center distance estimate is:

`C = (G + O) / 2`

This formula cancels the two opening diameters **when the contacts are on the relevant centerline**. Real M3 threads, knurls, chamfers, irregular bore edges, jaw shape and limited access make the result approximate. Do not place the inside jaws against unrelated thread flanks and assume metrology-grade precision. Repeat the reading after releasing/reseating the caliper; note variability. On a tiny insert bore this method may not be physically practical.

### Method B — two equal M3 screws as accessible measurement posts

Thread matching, straight M3 screws into two separated inserts. Measure the **outermost span** across the screw shanks (`O`) and the **inner gap** between them (`G`), at the same height above the plate; estimate `C = (G + O) / 2`. Prefer smooth, equal-diameter shank sections when available; fully threaded screw surfaces are less repeatable. Do not tighten screws to force them upright. Screw clearance, thread play and any tilt create uncertainty, increasing with measurement height. Repeat at a second height to detect tilt; if readings differ, do not treat their average as a verified center position.

### Method C — two-screw mating coupon (functional cross-check)

Use a mating test plate with independently inspected holes at an 8 mm multiple, ideally 32 mm apart. Start both screws by hand without prying or bending the plate. A successful fit demonstrates practical assembly with that plate, **not** an independent measurement unless its hole locations are independently known.

**Measurement hygiene:** zero and clean the caliper, measure after full cooling, align jaws consistently, do not compress the plastic, measure multiple pairs and directions, record actual values and method. A caliper display resolution of 0.01 mm does not imply ±0.01 mm accuracy.

## 7. Troubleshooting: tune only the relevant generator control

| Observed result | Likely investigation | Next trial |
|---|---|---|
| LEGO too tight *before* insertion | Skirt OD, flow, first-layer expansion | Slightly reduce skirt OD or correct print profile |
| LEGO too loose *before* insertion | Skirt OD, shrinkage, geometry | Slightly increase skirt OD, reprint |
| LEGO fits before, too tight *after* | Heat-set expansion or out-of-round tube | Adjust pilot/insert technique; if needed reduce initial skirt OD |
| LEGO fits before, too loose *after* | Heat deformation, tube collapse or softened contact geometry | Inspect insertion process and wall thickness; reprint, possibly adjust OD |
| Insert tilts or breaks out | Pilot bore mismatch, insufficient wall or insertion force | Reassess pilot size, tube wall and technique; do not force installation |
| Measured 32 mm span deviates | Printer X/Y scale, material effects, measuring method, heat distortion | Confirm calibration and inspect both before/after readings; **never change nominal grid pitch in the OSSMI generator** |
| One screw works, two bind | Center offset, insert tilt or mating-hole error | Diagnose with 32 mm baseline and second mounting coupon |

Adjust **one significant variable per trial**, and print a fresh coupon. If the available wall thickness is insufficient for an insert of the selected outer diameter, reject that insert/geometry combination rather than trying to force it into place.

## 8. Suggested maker record

```text
OSSMI-S FDM / M3 HEAT-SET CALIBRATION RECORD
Date:
OSSMI standard + generator revision:
Printer / slicer / material / nozzle / layer height / orientation:
Coupon grid dimensions:
Insert M3 type / manufacturer / outside diameter / length:
Installation tip and procedure / temperature if known:
Generator fixed pitch: X=8.00 mm; Y=8.00 mm
Generator skirt OD / pilot bore / plate edge margin:
LEGO reference item (ordinary genuine construction-set piece):
Before insertion — LEGO fit (5 cycles):
Before insertion — skirt OD readings / insert grid readings:
After cooling — skirt OD readings / delta:
After insertion — LEGO fit (5 cycles):
After insertion — M3 axial center spacings X: 8 mm / 32 mm:
After insertion — M3 axial center spacings Y: 8 mm / 32 mm:
Diagonal / squareness observation (optional):
Center measurement method and repeatability:
M3 screw finger-start / alignment / insert retention observations:
Two-screw functional coupon result (optional):
Defects, corrections, photographs:
Final classification: PASS / FAIL / NOT FULLY VERIFIED
```

**PASS** requires successful LEGO fit **after insertion**, satisfactory M3 screw engagement and evidence of grid alignment appropriate to the intended assembly. **NOT FULLY VERIFIED** means a required check was omitted or no useful measurement could be made; it must not be presented as fully validated. Numerical pitch tolerances and load ratings await experimental validation.

## 9. Safety and scope limits

Friction fit to a LEGO piece and successful M3 engagement are **not proof of vibration resistance, shock survival, fastener pull-out strength, thermal cycling performance or a safety rating**. For vehicle use, elevated mounts, valuable devices or equipment that could injure someone when detached, employ and validate an appropriate positive mechanical retainer. Hot inserts and soldering tools can burn users; follow tool and material safety procedures. OSSMI is independent of the LEGO Group.
