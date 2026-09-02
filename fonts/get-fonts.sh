#!/usr/bin/env bash
# Fetch the three typefaces the Lumon theme uses into ~/.local/share/fonts.
# All three are SIL Open Font License 1.1 (see FONTS.md).
set -euo pipefail

DEST="$HOME/.local/share/fonts"
mkdir -p "$DEST"

get() { echo ":: $1"; curl -fsSL -A 'omarchy-lumon-assets' -o "$DEST/$1" "$2"; }

get Michroma-Regular.ttf \
  'https://github.com/google/fonts/raw/main/ofl/michroma/Michroma-Regular.ttf'
get 'Orbitron[wght].ttf' \
  'https://github.com/google/fonts/raw/main/ofl/orbitron/Orbitron%5Bwght%5D.ttf'
get 'IBMPlexSans[wght].ttf' \
  'https://github.com/google/fonts/raw/main/ofl/ibmplexsans/IBMPlexSans%5Bwght%5D.ttf' \
  || get IBMPlexSans-Regular.ttf \
     'https://github.com/google/fonts/raw/main/ofl/ibmplexsans/IBMPlexSans-Regular.ttf'

fc-cache -f "$DEST" >/dev/null 2>&1 || true
echo "Done -> $DEST"
