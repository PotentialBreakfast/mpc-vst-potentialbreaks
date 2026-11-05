# Changelog

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
