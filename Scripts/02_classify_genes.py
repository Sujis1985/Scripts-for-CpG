import pandas as pd
import sys
import os

file = sys.argv[1]

# Extract filename without path
basename = os.path.basename(file)
species = basename.replace("_CpG_density.csv", "")

df = pd.read_csv(file)

q1 = df["CpG_density_per_kb"].quantile(0.25)
q3 = df["CpG_density_per_kb"].quantile(0.75)

def classify(x):
    if x >= q3:
        return "CpG-rich"
    elif x <= q1:
        return "CpG-poor"
    else:
        return "CpG-moderate"

df["CpG_class"] = df["CpG_density_per_kb"].apply(classify)

out = f"results/{species}_CpG_gene_classes.csv"
df.to_csv(out, index=False)

print(f"✅ CpG gene classification completed for {species}")
