#!/usr/bin/env python3
"""Run the acceptance tests embedded in the modules.

A test is a fenced python block whose first line is `# acceptance-test`.

    python tools/extract_tests.py              # every module
    python tools/extract_tests.py MC-05 MC-06  # selected modules
    python tools/extract_tests.py --pkg PATH   # folder that CONTAINS your starmc/ package (default: repo root)
"""
import re, subprocess, sys, tempfile, pathlib, time

root = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
pkg = root
if "--pkg" in args:
    i = args.index("--pkg")
    pkg = pathlib.Path(args[i + 1]).resolve()
    del args[i:i + 2]

mods = sorted((root / "modules").glob("MC-*.md"))
if args:
    mods = [m for m in mods if any(m.name.startswith(a) for a in args)]

fence = re.compile(r"^```python\n(# acceptance-test\n.*?)^```", re.S | re.M)
failed = 0
for m in mods:
    blocks = fence.findall(m.read_text(encoding="utf-8"))
    if not blocks:
        print(f"{m.name}: no acceptance test")
        continue
    for k, code in enumerate(blocks, 1):
        with tempfile.TemporaryDirectory() as d:
            f = pathlib.Path(d) / "t.py"
            f.write_text(f"import sys\nsys.path.insert(0, {str(pkg)!r})\n" + code, encoding="utf-8")
            t = time.time()
            r = subprocess.run([sys.executable, "-I", str(f)], capture_output=True, text=True)
        ok = r.returncode == 0
        print(f"{m.name} [{k}]: {'PASS' if ok else 'FAIL'} ({time.time() - t:.1f}s)")
        if not ok:
            failed += 1
            print((r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else "")
sys.exit(1 if failed else 0)
