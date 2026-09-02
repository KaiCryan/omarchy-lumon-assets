#!/usr/bin/env python3
"""Tiny image -> ASCII converter. Uses ImageMagick to read pixels (no PIL needed).
Usage: img2ascii.py <image> <cols> [--alpha] [--ramp " .:-=+*#%@"] [--invert]
--alpha : use the alpha channel as the mask (for white-on-transparent logos)
"""
import subprocess
import sys

RAMP = " .:-=+*#%@"


def pixels(path, cols):
    # aspect: terminal cells are ~2x taller than wide
    out = subprocess.run(
        ["magick", path, "-resize", f"{cols}x", "-colorspace", "sRGB",
         "-define", "txt:compliance=SVG", "txt:-"],
        capture_output=True, text=True, check=True,
    ).stdout
    grid = {}
    W = H = 0
    for line in out.splitlines():
        if line.startswith("#") or ":" not in line:
            continue
        coord, rest = line.split(":", 1)
        x, y = (int(v) for v in coord.strip("() ").split(","))
        W = max(W, x + 1)
        H = max(H, y + 1)
        # rest looks like "(r,g,b,a)  #hex  name" — pull the srgba tuple
        tup = rest.strip().split("(", 1)[1].split(")", 1)[0].split(",")
        r, g, b = (float(tup[i].strip().rstrip("%")) for i in range(3))
        a = float(tup[3].strip().rstrip("%")) if len(tup) > 3 else 255.0
        # magick may emit 0-255 or 0-100%
        if "%" in rest:
            r, g, b, a = r * 2.55, g * 2.55, b * 2.55, a * 2.55
        grid[(x, y)] = (0.299 * r + 0.587 * g + 0.114 * b, a)
    return grid, W, H


def main():
    args = sys.argv[1:]
    path = args[0]
    cols = int(args[1]) if len(args) > 1 else 100
    use_alpha = "--alpha" in args
    invert = "--invert" in args
    ramp = RAMP
    if "--ramp" in args:
        ramp = args[args.index("--ramp") + 1]

    grid, W, H = pixels(path, cols)
    rows = max(1, round(H * 0.5))  # correct for cell aspect
    lines = []
    for ry in range(rows):
        y = min(H - 1, round(ry * H / rows))
        row = []
        for x in range(W):
            lum, a = grid.get((x, y), (0, 0))
            v = (a / 255.0) if use_alpha else (lum / 255.0)
            if invert:
                v = 1.0 - v
            row.append(ramp[min(len(ramp) - 1, int(v * (len(ramp) - 1) + 0.5))])
        lines.append("".join(row).rstrip())
    print("\n".join(lines))


if __name__ == "__main__":
    main()
