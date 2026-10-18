# %% [markdown]
# # Example 03: find and download NICER data (NEEDS NETWORK; untested by the guide's author)
# usage: python ex03_query_download.py crab            # list sequences
#        python ex03_query_download.py crab 4142010107 # also download one obsid
# %%
import sys
from _common import *
from nicerkit import archive

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "crab"
    tab = archive.find_obs(target, radius_arcmin=5.0)
    print(tab.colnames)
    archive.summarize_obs(tab)
    if len(sys.argv) > 2:
        obsid = int(sys.argv[2])
        ob, tm = archive._col(tab, "obsid"), archive._col(tab, "time")
        row = [i for i in range(len(tab)) if int(tab[ob][i]) == obsid][0]
        print(archive.download_obs(obsid, tab[tm][row], dest="data"))
