#!/usr/bin/env python3
"""Generate a simple OSSMI host (socket-side) OpenSCAD model.
Usage:
    python ossmi_host.py 8 5

    to convert scad to stl
    openscad -o ossmi_host_8x5-2.stl ossmi_host_8x5.scad
Dimensions in millimeters. No third-party Python packages required.
"""
import argparse
from pathlib import Path

PITCH = 8.0
EDGE_ALLOWANCE = 0.2
HEIGHT = 3.0


def build_scad(nx: int, ny: int) -> str:
    width = nx * PITCH - EDGE_ALLOWANCE
    length = ny * PITCH - EDGE_ALLOWANCE
    return f'''// OSSMI host plate - prototype geometry (not yet fit-validated)
// {nx} x {ny} stud positions, 8 mm pitch; XY dimensions: {width:g} x {length:g} mm
// Host underside receiver: recessed cavity + clutch tubes; flat outer face.
$fn = 64;

nx = {nx};
ny = {ny};
pitch = {PITCH:g};
height = {HEIGHT:g};
width = {width:g};
length = {length:g};

skin = 1.0;            // top skin thickness
wall = 1.5;            // perimeter wall thickness
tube_od = 6.51;         // initial underside tube OD, unvalidated
tube_id = 4.4;         // illustrative tube bore, unvalidated

// Z=0: underside/receiving face; Z=height: exterior face with through-holes.
// Bore cylinders are cut through the complete assembled solid,
// so the 0.8 mm outer skin is perforated as well.
difference() {{
    union() {{
        // Outer shell: top skin and continuous perimeter skirt.
        difference() {{
            cube([width, length, height]);
            translate([wall, wall, -0.01])
                cube([width - 2*wall, length - 2*wall, height - skin + 0.01]);
        }}

        // Underside clutch tubes between four stud positions.
        for (ix = [1 : nx - 1])
            for (iy = [1 : ny - 1])
                translate([ix*pitch - {EDGE_ALLOWANCE/2:g}, iy*pitch - {EDGE_ALLOWANCE/2:g}, 0])
                    cylinder(h=height-skin, d=tube_od);
    }}

    // Through-holes continue through the tubes AND the 0.8 mm top skin.
    for (ix = [1 : nx - 1])
        for (iy = [1 : ny - 1])
            translate([ix*pitch - {EDGE_ALLOWANCE/2:g}, iy*pitch - {EDGE_ALLOWANCE/2:g}, -0.01])
                cylinder(h=height+0.02, d=tube_id);
}}
'''


def main() -> None:
    p = argparse.ArgumentParser(description='Generate a 3-mm OSSMI host plate as OpenSCAD.')
    p.add_argument('nx', type=int, help='Number of stud positions along X')
    p.add_argument('ny', type=int, help='Number of stud positions along Y')
    p.add_argument('-o', '--output', type=Path, help='Output .scad file')
    args = p.parse_args()
    if not 1 <= args.nx <= 100 or not 1 <= args.ny <= 100:
        p.error('nx and ny must be between 1 and 100')
    target = args.output or Path(f'ossmi_host_{args.nx}x{args.ny}.scad')
    if target.suffix.lower() != '.scad':
        p.error('output filename must end with .scad')
    target.write_text(build_scad(args.nx, args.ny), encoding='utf-8')
    print(f'{target}: {args.nx * PITCH - EDGE_ALLOWANCE:g} x '
          f'{args.ny * PITCH - EDGE_ALLOWANCE:g} x {HEIGHT:g} mm')


if __name__ == '__main__':
    main()
