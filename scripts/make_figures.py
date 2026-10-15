"""Run every fig_*.py script in this folder. Usage: python3 scripts/make_figures.py"""
import glob
import os
import runpy
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
scripts = sorted(glob.glob(os.path.join(here, "fig_*.py")))
only = sys.argv[1:]
for s in scripts:
    name = os.path.basename(s)
    if only and not any(o in name for o in only):
        continue
    print("==", name)
    runpy.run_path(s, run_name="__main__")
