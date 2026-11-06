# OSSMI — FDM Fit Calibration Guide

**Status:** Draft / community validation guide  
**Scope:** FDM-printed OSSMI host (receiving) and adapter (stud) interfaces  
**Primary acceptance criterion:** Functional fit with ordinary, mass-produced genuine LEGO construction-set elements  
**Secondary method:** Dimensional inspection when a reference piece is unavailable

## 1. Purpose

OSSMI aims for interchangeable interfaces made by different people, using different printers and materials. The important result is **a repeatable mechanical fit against a common physical reference**, not merely matching a number in CAD or optimizing a print for one particular machine.

### Why ordinary LEGO pieces are the reference

The reference is **any suitable ordinary, mass-produced genuine LEGO construction-set element** with the standard mating geometry required by the test: a brick or plate taken from a regular LEGO set is sufficient. **No special reference block, precision gauge, laboratory master, or dedicated calibration part is required.**

This choice is deliberate. Genuine LEGO System construction elements are manufactured in large quantities with highly consistent mating geometry. Their practical uniformity and wide availability make them a useful shared physical benchmark for OSSMI fit tests across makers and printers. They are not claimed to be mathematically identical or a certified metrology standard; different element types can have different underside structures, and wear affects fit.

For this purpose, "any" means any **undamaged, unmodified, authentic LEGO System brick or plate with the appropriate mating features**—not literally every LEGO product or element shape. Use an element with standard studs for Test A, and one with a compatible receiving underside for Test B. A caliper remains useful for diagnosing failures, documenting dimensions, and performing a preliminary dimensional check when no suitable LEGO element is available.

> **Important:** These are **ordinary consumer LEGO construction-set parts**, not purpose-made reference blocks. They act as *functional calibration references*, not official OSSMI-certified gauges. Passing this test is evidence of fit with the particular reference elements tested; it does not certify every possible LEGO/OSSMI combination or mechanical load case.

## 2. What to prepare

- Freshly printed OSSMI **host** sample (receiving geometry) and OSSMI **adapter** sample (studs).
- **Reference A:** any ordinary genuine LEGO System brick or plate from a regular construction set with several exposed standard studs, to test the OSSMI host; no specially manufactured reference element is needed.
- **Reference B:** any ordinary genuine LEGO System brick or plate from a regular construction set with a compatible underside receiving geometry, to test the OSSMI adapter. Prefer a 2-stud-wide brick/plate with internal supports for a multi-stud test; check that the underside actually has the receiving features needed for the chosen sample.
- Optional but recommended: digital caliper, marker and notes, a second reference LEGO piece to rule out a worn/damaged sample.

Avoid damaged, heavily worn, modified, or visibly deformed reference elements. Test ordinary standard LEGO-System-style geometry, not DUPLO or other incompatible families.

## 3. Print small test coupons first

Print small host and adapter coupons before a full device enclosure. Use at least a **2×3 or 2×4 interface area**, where geometry permits, so the test checks **grid alignment as well as a single local fit**. If a particular host underside relies on internal tubes, use a sample that actually includes those tubes (not a 1×N strip).

Use the normal FDM workflow intended for production parts. Keep the print orientation, material, nozzle and slicer profile recorded with the test result. The procedure is **printer-independent**; it does not prescribe one machine's compensation settings.

Remove brims, supports and loose strings that obstruct the interface. Do not sand, drill or heat-form the mating features before the initial test: that would hide the as-printed result.

## 4. Primary test: reference-element fit

### Test A — OSSMI host on genuine LEGO studs

1. Align the host receiving side with the studs of Reference A.
2. Press together by hand, **straight and evenly**; do not twist or use tools.
3. Check whether it reaches a consistent seated position without excessive force or visible deformation.
4. Gently lift, tilt and lightly shake the joined parts over a safe surface. Check for noticeable wobble or unintended separation.
5. Separate by hand without prying tools, cracking sounds, whitening, or damage.
6. Repeat assembly/disassembly **five times**, checking for changes in fit.

### Test B — OSSMI adapter studs into genuine LEGO underside

Repeat the same six checks, this time inserting the printed adapter's studs into Reference B's underside. Confirm that the reference underside supports the chosen stud arrangement; not every LEGO element's bottom geometry is equivalent.

### Record the outcome of each test

| Result | Observable fit | Decision |
|---|---|---|
| **PASS** | Seats fully by normal hand pressure; no obvious wobble or accidental release during a gentle handling check; separates by hand without damage; remains consistent over five cycles | Accept for prototype fit |
| **TOO TIGHT** | Does not seat fully, requires excessive force, visibly deforms, or cannot be removed safely by hand | Adjust and reprint |
| **TOO LOOSE** | Noticeable rocking, easily falls off, or disengages with very light handling | Adjust and reprint |
| **INCONSISTENT** | Only some positions engage, multi-stud alignment binds, or fit changes markedly across five cycles | Check grid, geometry and print quality; reprint |

**PASS is a qualitative fit test, not a certified pull-force or load rating.** For a use case involving vibration, vehicle mounting, overhead loads or valuable equipment, design and test an additional positive retention mechanism as needed. LEGO-style friction alone must not be treated as safety-rated retention.

## 5. Troubleshooting and iteration

If the host is **too tight** on LEGO studs, inspect receiving cavities, tube walls, elephant's foot and over-extrusion. If it is **too loose**, inspect the actual receiving contact surfaces and dimensional shrinkage. For the adapter, test whether the **printed studs** are oversized (tight) or undersized (loose). If a multi-stud sample binds even though a single stud fits, check the **8 mm grid pitch** and accumulated spacing error.

Change **one relevant geometry or print-process variable at a time**, then print a fresh coupon and repeat both tests. Do not change the published OSSMI nominal interface dimensions merely to mask one printer's errors; keep experimental compensation separate from the nominal design and document it.

It is possible for a printed OSSMI host and adapter to mate well **with each other** while both are incompatible with the common reference. For that reason, **self-mating is a supplementary test only**, never the sole acceptance test.

## 6. Secondary route: caliper inspection

If genuine LEGO reference elements are unavailable, use a caliper to check the coupon against the **current revision of the OSSMI CAD specification**. Document measured values and print conditions. For the present prototype generators, useful nominal checks include:

| Feature | Prototype nominal value |
|---|---:|
| Grid pitch | 8.0 mm |
| Adapter stud diameter | 4.8 mm |
| Adapter stud height above base | 1.8 mm |
| Adapter base thickness | 0.8 mm |
| Host internal tube outside diameter | 6.5 mm |
| Host tube bore (through-hole) diameter | 4.8 mm |
| Host overall thickness | 3.0 mm |
| Nominal rectangular outline | `N × 8 − 0.3 mm` per axis |

These are **prototype design targets, not independently validated FDM tolerance limits**. In particular, measuring a 4.8 mm diameter does not by itself prove good frictional fit. The caliper route provides **provisional dimensional conformity**, not a verified functional PASS. When a physical LEGO reference becomes available, repeat Section 4.

Do not infer compliance from a single diameter: wall geometry, contact surfaces, pitch, material elasticity and layer quality affect engagement. Measure in several places and note any systematic deviation or asymmetry.

## 7. Optional cross-check: OSSMI-to-OSSMI

After both reference tests pass, assemble a printed OSSMI host and adapter from the same or different sources. Confirm seating, multi-stud alignment, retention and safe removal. Ideally repeat with coupons printed by **another maker, printer or material** to test actual interchangeability beyond a single setup.

## 8. Shareable calibration record

```text
OSSMI FDM FIT RECORD
Date:
OSSMI spec / generator revision:
Host coupon size:
Adapter coupon size:
Material(s):
Printer / slicer profile (optional but helpful):
Orientation / layer height:
Reference A (LEGO stud element):
Reference B (LEGO receiving element):
Test A — host to LEGO studs: PASS / TOO TIGHT / TOO LOOSE / INCONSISTENT
Test B — adapter to LEGO underside: PASS / TOO TIGHT / TOO LOOSE / INCONSISTENT
Five assembly cycles completed? YES / NO
Optional caliper measurements:
Optional OSSMI-to-OSSMI test:
Notes / photos / adjustments:
```

## 9. Minimum statement of compatibility

Only describe a printed OSSMI pair as **“LEGO-reference fit tested”** when **both Test A and Test B pass**, with the reference element types identified. If only caliper inspection was performed, describe it as **“dimensionally inspected; physical reference fit not yet verified.”**

This keeps the public interface definition stable while giving makers a low-cost, reproducible way to validate the actual fit.
