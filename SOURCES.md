# Sources & attribution

This repo is a small kit for a personal, non-commercial *Severance* desktop
theme. "Lumon Industries", "Macrodata Refinement", the Lumon globe and wordmark
are from the TV series *Severance* (Apple TV+); this is unofficial fan work.

## In this repo

- `ascii/` — ASCII renderings of the Lumon globe / wordmark / block, generated
  with `tools/img2ascii.py` from the vector logo below. Hand-tuned afterwards.
- `ascii/mdr-digits.txt` — a field of "scary" numbers for the refinement scenes.
- `tools/img2ascii.py` — tiny image → ASCII converter (ImageMagick + stdlib,
  no PIL). Original.

## Not bundled (get them yourself)

- **Vector Lumon logos** (globe, wordmark, block, inverted) — free for
  non-commercial use from <https://www.valencygraphics.com> ("Severance /
  Lumon" resources). Drop the globe PNG next to `img2ascii.py` to regenerate
  the ASCII.
- **Fonts** — see `fonts/FONTS.md` / `fonts/get-fonts.sh` (all SIL OFL 1.1).
