import pandas as pd
import sys
import os

enc_file = sys.argv[1]
cai_file = sys.argv[2]
species = sys.argv[3]

# Load ENC + GC3
enc = pd.read_csv(enc_file)
enc = enc.rename(columns={
    "Gene_ID": "GeneID",
    "ENC_obs": "ENC"
})

# Keep only required columns
enc = enc[["GeneID", "ENC", "GC3s"]]

# Load CAI
cai = pd.read_csv(cai_file)
cai = cai.rename(columns={"Gene": "GeneID"})

# Merge ENC + CAI
merged = pd.merge(enc, cai, on="GeneID", how="inner")

out = f"results/{species}_Objective2_codonbias_clean.csv"
merged.to_csv(out, index=False)

print(f"✅ Clean codon bias file created for {species}")
