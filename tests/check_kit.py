#!/usr/bin/env python3
"""Reads back what tests/test_kit.c wrote, the way the MPC does, and checks it (see src/kit_writer.h)."""
import gzip, json, os, sys, wave

d = sys.argv[1]
fails = 0


def check(ok, msg):
    global fails
    if not ok:
        fails += 1
        print("FAIL:", msg)


check(gzip.open(os.path.join(d, "roundtrip.gz")).read() == open(os.path.join(d, "roundtrip.bin"), "rb").read(), "gzip round trip")
for name in ("Funky Drummer take 1 98", "Funky Drummer take 1 98 2"):
    xpm = os.path.join(d, name + ".xpm")
    raw = gzip.open(xpm).read().decode("utf-8")
    head, body = raw.split("{", 1)
    lines = head.rstrip("\n").split("\n")
    check(lines[0] == "ACVS" and lines[2] == "SerialisableProgramData" and lines[3] == "json", "header %r" % lines)
    doc = json.loads("{" + body)["data"]
    check(doc["name"] == name, "name %r" % doc["name"])
    ins = doc["drum"]["instruments"]
    check(len(ins) == 128, "128 pads, got %d" % len(ins))
    pdir = os.path.join(d, name + "_[ProgramData]")
    names = []
    for p in range(16):
        l = ins[p]["layersv"][0]
        if p == 5:
            check(l["sampleName"] == "" and l["sampleFile"] == "", "pad 6 should be empty")
            continue
        sn = "%s %02d" % (name, p + 1)
        names.append(sn)
        check(l["sampleName"] == sn and l["sampleFile"] == sn + ".wav", "pad %d sample %r" % (p + 1, l["sampleName"]))
        with wave.open(os.path.join(pdir, sn + ".wav")) as w:
            check(w.getnchannels() == 2 and w.getframerate() == 44100 and w.getsampwidth() == 2, "wav format pad %d" % (p + 1))
            check(l["sliceInfo"]["End"] == w.getnframes() - 1, "pad %d End %d vs %d frames" % (p + 1, l["sliceInfo"]["End"], w.getnframes()))
            check(w.getnframes() == 4410 + 997 * p, "pad %d frames" % (p + 1))
        check(abs(ins[p]["tempo"] - 97.5) < 1e-6, "pad tempo %r" % ins[p]["tempo"])
    for p in range(16, 128):
        check(ins[p]["layersv"][0]["sampleName"] == "", "pad %d should be empty" % (p + 1))
    check([s["name"] for s in doc["samples"]] == names, "samples list")
    check(all(s["path"] == s["name"] + ".wav" for s in doc["samples"]), "sample paths")
    seeds = {x["layersv"][0]["sliceIncrementRngSeed"] for x in ins}
    check(len(seeds) > 100, "seeds differ between pads (%d distinct)" % len(seeds))
    # same shape as the MPC's own (the template's keys, in its order), pad for pad
    tpl = json.loads("{" + gzip.open(sys.argv[2]).read().decode("utf-8").split("{", 1)[1])["data"] if len(sys.argv) > 2 else None
    if tpl:
        check(list(doc.keys()) == list(tpl.keys()), "top-level keys differ from the MPC's")
        check(list(ins[0].keys()) == list(tpl["drum"]["instruments"][0].keys()), "pad keys differ from the MPC's")
        check(list(ins[0]["layersv"][0].keys()) == list(tpl["drum"]["instruments"][0]["layersv"][0].keys()), "layer keys differ")
    print("%s: %d bytes (%.0f KB packed)" % (name, len(raw), os.path.getsize(xpm) / 1024))
print("ALL PASSED" if not fails else "%d FAILED" % fails)
sys.exit(1 if fails else 0)
