import pandas as pd
import glob
import os

rich_files = glob.glob("results/*_CpG_rich_RSCU.csv")

for rf in rich_files:
    sp = os.path.basename(rf).replace("_CpG_rich_RSCU.csv", "")
    pf = f"results/{sp}_CpG_poor_RSCU.csv"

    rich = pd.read_csv(rf)
    poor = pd.read_csv(pf)

    merged = rich.merge(poor, on="Codon", suffixes=("_CpG_rich","_CpG_poor"))
    merged.to_csv(f"results/{sp}_RSCU_comparison.csv", index=False)

    print(f"✅ Merged RSCU for {sp}")
