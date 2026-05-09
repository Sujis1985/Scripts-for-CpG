import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import os

files = glob.glob("results/*_CpG_density.csv")
all_data = []

for f in files:
    species = os.path.basename(f).replace("_CpG_density.csv", "")
    
    density = pd.read_csv(f)
    codon = pd.read_csv(f"results/{species}_Objective2_codonbias_clean.csv")

    merged = pd.merge(density, codon, on="GeneID")
    merged["Species"] = species
    all_data.append(merged)

df = pd.concat(all_data)

# Create GC3 bins
def gc3_bin(x):
    if x < 40:
        return "Low GC3"
    elif x < 60:
        return "Medium GC3"
    else:
        return "High GC3"

df["GC3_category"] = df["GC3s"].apply(gc3_bin)

# Enforce logical order on x-axis
order = ["Low GC3", "Medium GC3", "High GC3"]

plt.figure(figsize=(8,6))
sns.boxplot(
    x="GC3_category",
    y="CpG_density_per_kb",
    data=df,
    order=order
)

plt.title("CpG density across GC3 categories")
plt.xlabel("GC3 category")
plt.ylabel("CpG density per kb")

plt.tight_layout()
plt.savefig("figures/Figure6_GC3_controlled_CpG_density.png", dpi=300)

print("✅ GC3-controlled CpG analysis completed")
