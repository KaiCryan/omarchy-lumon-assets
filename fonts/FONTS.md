# Fonts

The Lumon theme repos reference three typefaces. They're not bundled here —
`get-fonts.sh` pulls them from upstream. All three are under the
**SIL Open Font License 1.1**.

| Font | Role | Upstream |
|---|---|---|
| **Michroma** (Vernon Adams) | wide geometric caps — a free stand-in for the Lumon wordmark face (Manifold Extended CF) | <https://fonts.google.com/specimen/Michroma> |
| **Orbitron** (Matt McInerney) | alternate display caps | <https://fonts.google.com/specimen/Orbitron> |
| **IBM Plex Sans** (IBM) | body / captions | <https://github.com/IBM/plex> · <https://fonts.google.com/specimen/IBM+Plex+Sans> |

The wallpaper and greeting generators resolve fonts through `fontconfig` and
fall back to generic `sans-serif` / `monospace` if these aren't installed, so
this step is optional — it just won't look quite right.
