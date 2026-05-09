import pandas as pd
import sys
import os

cpg_file = sys.argv[1]
codon_file = sys.argv[2]

species = os.path.basename(cpg_file).replace("_CpG_gene_classes.csv","")

cpg = pd.read_csv(cpg_file)
codon = pd.read_csv(codon_file)

merged = pd.merge(cpg, codon, on="GeneID", how="inner")

out = f"results/{species}_Objective2_merged.csv"
merged.to_csv(out, index=False)

print(f"✅ Objective 2 merged file created for {species}")
