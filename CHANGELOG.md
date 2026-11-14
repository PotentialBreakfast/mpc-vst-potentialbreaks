# Changelog

## 1.6.0 (2026-11)
- **MANUAL page.** The plugin's manual is now on the MPC's screen: tap **MANUAL**, then the page buttons along the top (what it does, the controls, how it works with the other PotentialSuite plugins, and good-to-know notes). The full PotentialSuite manual is on the [PotentialSuite page](https://github.com/PotentialBreakfast/potential-plugins).
- One parameter was added at the end of the list (Manual Page); saved projects open as before. Sound and controls are unchanged.

## 1.5.0 (2026-11)
- **BROWSE page**: pick the exact break you want. It lists the breaks in the current library 10 at a time; tap a name to load it. **PAGE UP** / **PAGE DOWN** move through the list, **LIBRARY** switches folders without loading anything, and the break that's playing is lit. It opens on the page with the current break.
- Two pages now: BREAKS (as before) and BROWSE. Fourteen parameters were added at the end of the list for the page; saved projects open as before.

## 1.4.0 (2026-11)
- **ROLL**: one tap for a random break played a random way. **MILD** chops it on the grid, in order. **MEDIUM** may also chop on the HITS, change the loop length, shuffle the pads and move the pitch a little. **WILD** shuffles every time, can switch the tempo mode and pitches up to 7 semitones either way. RANDOM BREAK still just picks a break.
- **GRID chop now always cuts on the beat.** Before, a loop that wasn't 1, 2, 4 or 8 bars long was cut into 8 or 16 equal pieces, so the slices (and the MIDI from SAVE KIT and SAVE GROOVE) fell between the beats: a 7-bar loop gave slices 1 3/4 beats long. Now each slice is a whole number of beats (or a half or quarter beat), as many as fit on the pads: a 7-bar loop gives 14 slices of 2 beats. 1, 2, 4 and 8 bar loops are cut as before.
- The DIG panel is rearranged to fit ROLL. Two parameters were added at the end of the list (Roll, Roll Wildness); saved projects open as before.

## 1.3.0 (2026-11)
- **SAVE KIT**: one tap saves the 16 pads as a real **MPC drum program**: each pad as a WAV, as you hear it (at your tempo, pitch and shuffle), on pads A01-A16, with the groove as a MIDI file beside it. Load it like any program. It goes to `PotentialBreaks/Kits` on your breaks' drive, or to the folder named in `PotentialBreaks/kit-folder.txt`. Needs MPC OS 3.10.1 or later (the program format it writes).
- The DIG panel has room for it: RANDOM BREAK on top, then SAVE KIT, SAVE GROOVE, PLAY LOOP and RESCAN.

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
