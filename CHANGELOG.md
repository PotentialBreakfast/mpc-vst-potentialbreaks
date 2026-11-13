# Changelog

## 1.2.2 (2026-11)
- **CPU figure recorded.** Measured on an MPC One with the Open MPC bench: **PASS**, 1.1% of an audio block at the 99th percentile and 2.5% at worst, so it runs comfortably alongside a full project. It shows on the catalog card and in INSTALL.md.
- Nothing else changed: same sound, controls and saved projects as 1.2.1.

## 1.2.1 (2026-11)
- **Ready for MPC OS 3.10.1's plugin folders.** Every download now carries the `plugin.json` that MPC OS 3.10.1 looks for, so the plugin folder can be copied by hand straight into `VST2 Plugins`.
- **Gen2 MPCs in the Open MPC catalog.** A separate 64-bit download (`-mpc-aarch64.zip`), so the Plugin Manager can install it on Gen2 MPCs, and the catalog's 3.10.1 download (`-mpc-sdk.zip`).
- Built with the current Open MPC kit. Sound, controls and saved projects are unchanged.

## 1.2.0 (2026-11)
- **Three looks.** A new default look, **Print Plate** (a warm printed panel), plus **Night Rack** (dark rack unit) and **Colour Block** (flat, big type), each in PotentialBreaks's own colour. Pick one with the big LOOK keys on the SETTINGS page; it shows the next time the plugin loads (take it off and add it again, or load your project again), and it is remembered on your MPC for every project.
- Sound, controls and saved projects are unchanged. One parameter was added at the end of the list (LOOK); it is never saved in a project.
- **Akai's plugin folder format** for MPC OS 3.10.1 and later: a second download (`-akai-vst2.zip`) with 32-bit and 64-bit builds, so it now also runs on Gen2 MPCs. Copy the folder into `VST2 Plugins` and turn on External Plugin Support: no hacking needed.

## 1.1.4 (2026-11)
- Fixed: pressing **STOP** or **Overdub** while the MPC was playing could load a random break. The MPC's host briefly "presses" a plugin's first parameter when it re-prepares audio, and that was RANDOM BREAK. That first slot now does nothing; RANDOM BREAK is a new parameter at the end. The button works the same.
- If you had automation or a Q-Link on RANDOM BREAK (unlikely), point it at the new **Random Break** parameter.

## 1.1.3 (2026-11)
- The plugin's name on its page now reads **PotentialBreaks** (was all capitals), matching its name in the MPC's plugin list. Nothing else changed.

## 1.1.2 (2026-11)
- New look: Barlow fonts, raised panels with soft shadows, glowing amber knob arcs, even-sized button labels and darker display wells.
- MIDI from other tracks can no longer change the plugin's settings (NRPN control is off). Q-Links and CC 20-35 still work.

## 1.1.1 (2026-11)
- First public release.
- Random break, PREV, NEXT and LIBRARY; long tracks are cut to random 1, 2 or 4 bar loops.
- Tempo read from the file name, or detected; Re-pitch and Stretch modes.
- Chop: Grid 8, Grid 16 (moved onto hits) or Hits; SHUFFLE and ORDER; CHOKE, PITCH and VOLUME.
- LEARN for pad mapping; PLAY LOOP; SAVE GROOVE (a MIDI file of the slice order).
- Finds breaks in `DRUM BREAKS LIBRARY`, in any top-level folder with "break" in its name, or in folders listed in `PotentialBreaks/folders.txt`; RESCAN.
- Only reads the first 3 minutes of a file, to protect the MPC's memory.
- Moved to its own repository (mpc-vst-potentialbreaks); the code is the same as in the earlier `potential-plugins` repo.
