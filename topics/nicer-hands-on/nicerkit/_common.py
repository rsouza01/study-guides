import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import matplotlib
if not os.environ.get("DISPLAY"):
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "figures")
os.makedirs(FIGDIR, exist_ok=True)


def savefig(fig, name):
    p = os.path.join(FIGDIR, name)
    fig.savefig(p, dpi=130, bbox_inches="tight")
    print("saved", os.path.relpath(p))
