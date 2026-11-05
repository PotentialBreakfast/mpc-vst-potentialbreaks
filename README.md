# PotentialBreaks

**Dig, chop, play.** Tap one button for a random drum break from your own library. It's sliced across 16 pads and matched to your project's tempo, ready to flip.

![PotentialBreaks's page on the MPC (new look)](docs/images/potentialbreaks.png)

*Instrument plugin · MPC OS 3.x · Gen1 (32-bit) · v1.1.2*

Free and open source (MIT), made by **PotentialBreaks**. It runs inside the MPC like its own instruments, with its own touchscreen page, Q-Link control and project recall, and no computer needed while you play.

**[Download the latest release](../../releases/latest)** · [Install guide](INSTALL-GUIDE.md) · [FAQ](FAQ.md) · [Ideas and bugs](../../issues/new/choose)

## What it does

- **RANDOM BREAK** picks a break from your library. **PREV** and **NEXT** step through them, and **LIBRARY** switches folders.
- **Long tracks** (a whole drum-library track, say) get a random 1, 2 or 4 bar loop cut from them, starting on a hit. Short files are used as they are.
- **Tempo** comes from the file name when it has one (`Funky Drummer 101bpm.wav` or `... 96 BPM.wav`). Otherwise it's measured.
- **CHOP** gives you 8 even slices, 16 even slices (moved onto the nearest hit), or the 16 strongest hits.
- **TEMPO** has two modes:
  - **Re-pitch** speeds the break up or slows it down to your tempo, like an old sampler.
  - **Stretch** keeps each slice at its own pitch and cuts it to length, the classic chopped-break method.
- **SHUFFLE** re-deals the slices across the pads, and **ORDER** puts them back.
- **PLAY LOOP** (or the pad after pad 16) plays the whole loop.
- **SAVE GROOVE** writes a MIDI file of the break's original slice order, so you can load it into a sequence and start from the real groove.
- **CHOKE**, **PITCH** (±12 semitones) and **VOLUME** are here too.
- Your project remembers the break, the chop, the pad order and the settings.

## Where it finds your breaks

You don't have to type any paths. It looks in three places:

1. **A folder called `DRUM BREAKS LIBRARY`** at the top of any drive (SD card, USB drive or SSD).
2. **Any folder at the top of a drive with "break" in its name**, such as `My Breaks` or `Breakbeats`.
3. **Folders you list yourself** in `PotentialBreaks/folders.txt`. The plugin creates this file on your breaks drive the first time it runs, with instructions inside. Put one folder per line, either a full path or a folder on that drive.

Every sub-folder becomes a **library** you can step through with LIBRARY. Files lying loose in a folder make a library of their own. After adding folders, tap **RESCAN**.

WAV and FLAC files are supported.

## Playing it from the pads

The pads play **MIDI notes 36–51** (and 0–15). If pad 1 doesn't play the first slice on your MPC, tap **LEARN** and then hit the pad you want as pad 1. The STATUS line shows the last note received, which helps with setup.

## Limitations

- **Only the first 3 minutes of a file are used.** This keeps the MPC's memory safe on huge files.
- **The tempo guess for unnamed files is 80–160 BPM.** A 70 BPM break may read as 140. Putting the BPM in the file name avoids this.
- **Stretch mode doesn't time-stretch.** Slices keep their pitch, so at a slower tempo you'll hear small gaps between hits. That's the classic sound, but it isn't a smooth stretch.
- **The automatic chop is a best guess.** On busy or swung breaks some slices may not land exactly on a hit. Try another CHOP mode.
- **8 voices**, and only 44.1 kHz playback.
- **The pads map like a keyboard.** The MPC treats a plugin track like a keyboard, so with some pad bank or octave settings pad 1 isn't note 36. LEARN fixes this.
- **SAVE GROOVE** writes to the first drive your breaks are on, in a `PotentialBreaks` folder.
- **Tested on an MPC One only**, and on Gen1 hardware only.

## Will it work on my MPC?

| | |
|---|---|
| **Tested on** | MPC One (first generation) with HAKAI 3.10 firmware |
| **Should work on** | Other first-generation (Gen1, 32-bit) standalone MPCs running **MPC OS 3.x**: One, Live, Live II, X |
| **Not yet** | Gen2 hardware (MPC One+, Live III, Key 37, XL and others): no build yet. **MPC OS 2.x**: not supported |
| **You need** | A way to install third-party plugins on your MPC (see below) |

The **Should work on** row is untested so far. If you try it on another model, please [tell me how it went](../../issues/new/choose).

## Install

**👉 [Step-by-step install guide](INSTALL-GUIDE.md)**: start here if it's your first plugin.

The short version:
1. Download `PotentialBreaks-<version>-mpc-armv7.zip` from [**Releases**](../../releases) and leave it zipped.
2. Install it with the free **MPC Plugin Installer** from [Open MPC](https://open-mpc.github.io/): connect, drop the zip in, press Install. Or install over SSH (see the guide).
3. **Save your project first.** Installing restarts the MPC app.
4. Find **PotentialBreaks** in the plugin (instrument) list.

Stuck? The [**FAQ**](FAQ.md) covers the common problems.

## Also good to know

- **Made by one person, tested on one MPC.** It works well for me, but you may hit something I haven't. Please tell me if you do.
- **Plugins must be allowed to run on your MPC.** Stock firmware doesn't load third-party plugins until it has been set up for them (see [Open MPC](https://open-mpc.github.io/)). After a firmware update, you may have to redo that setup.
- **No warranty.** It's free and comes as it is. Back up your projects.

## Ideas, bugs and criticism: all welcome

I make these for myself first, and I want them to be good for everyone else too, so **please tell me what you think**, including what you don't like.

- 💡 [Suggest a feature](../../issues/new?template=idea.yml)
- 🐛 [Report a bug](../../issues/new?template=bug.yml)

You don't need to be technical. Short messages are great. See [CONTRIBUTING.md](CONTRIBUTING.md) for more, including how to send code.

## More from PotentialBreaks

- **[PotentialPatina](https://github.com/PotentialBreakfast/mpc-vst-potentialpatina)**: Retro-colour insert effect: vinyl and tape noise, wobble, drive, bit-crush, tone and room in one box.
- **[PotentialWax](https://github.com/PotentialBreakfast/mpc-vst-potentialwax)**: Melodic sampler: pick or dig a song from your library, 16 cues found for you, matched to your tempo and key.
- **[PotentialNoise](https://github.com/PotentialBreakfast/mpc-vst-potentialnoise)**: Calibrated pink noise reference for mixing: one-tap RMS levels, mono/stereo, full or limited range, live meter.
- **[MPC TOOLS](https://github.com/PotentialBreakfast/mpc-tools)**: a free second-screen app for Windows: your MPC's screen live on your PC (and in OBS), file transfer, your PC's folders on the MPC, and one-click "save the last 60 seconds".

## Build it yourself

See [BUILD.md](BUILD.md).

## Credits

- Built on **[mpc-vst-plugins](https://github.com/sd88me/mpc-vst-plugins)** by sd88me (MIT), the open kit that makes MPC plugins possible: the plugin wrapper, skin builder and installer.
- Audio file reading by **[dr_libs](https://github.com/mackron/dr_libs)** (dr_wav and dr_flac) by David Reid (public domain / MIT-0).
- Fonts: **Barlow** and **Barlow Condensed** by Jeremy Tribby (SIL Open Font License 1.1), in `vst/skin/fonts/`.
- The dark look grew out of the theme I made for sd88me's Lucky Dip.
- Made with help from Claude (Anthropic).

Not affiliated with or endorsed by Akai Professional or inMusic. MPC is their trademark.

## Licence

[MIT](LICENSE): free to use, change and share, including in your own projects. Third-party parts keep their own licences ([THIRD_PARTY.md](THIRD_PARTY.md)).
