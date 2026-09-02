# omarchy-lumon-assets

Shared bits for the Lumon / *Severance* theme repos — ASCII art, the font list,
and the little tool that made the art.

```
ascii/        Lumon globe / wordmark / block as ASCII, + a field of MDR digits
fonts/        get-fonts.sh + FONTS.md (Michroma, Orbitron, IBM Plex Sans — OFL)
tools/        img2ascii.py — image -> ASCII (ImageMagick + stdlib only)
```

Nothing to "install". The other repos vendor what they need; this is the
source-of-truth kit and the place to regenerate the art from.

```sh
# regenerate the globe ASCII from a logo PNG
python3 tools/img2ascii.py lumon-globe.png 100 --ramp " .:-=+*#%@" > ascii/lumon-globe-100.txt
```

See `SOURCES.md` for attribution — this is unofficial *Severance* fan work.

## Related

- [omarchy-lumon-greeting](https://github.com/KaiCryan/omarchy-lumon-greeting) — terminal greeting
- [omarchy-lumon-screensaver](https://github.com/KaiCryan/omarchy-lumon-screensaver) — screensavers
- [omarchy-lumon-wallpapers](https://github.com/KaiCryan/omarchy-lumon-wallpapers) — wallpapers + hourly cycle
- [omarchy-lumon-lock](https://github.com/KaiCryan/omarchy-lumon-lock) — lock screen
- [omarchy-lumon-boot](https://github.com/KaiCryan/omarchy-lumon-boot) — Plymouth splash
- [omarchy-lumon-theme](https://github.com/KaiCryan/omarchy-lumon-theme) — colors, look'n'feel, branding
