import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob

dfs = []

for f in glob.glob("results/*_CpG_positional_distribution.csv"):
    species = f.split("/")[-1].replace("_CpG_positional_distribution.csv", "").replace("_", " ")
    df = pd.read_csv(f)

    # Assume equal-length partitions → CpG density proportional to counts
    mean_vals = {
        "5′ region": df["CpG_5prime"].mean(),
        "Gene body": df["CpG_middle"].mean(),
        "3′ region": df["CpG_3prime"].mean()
    }

    temp = pd.DataFrame({
        "Region": mean_vals.keys(),
        "CpG_density": mean_vals.values(),
        "Species": species
    })

    dfs.append(temp)

plot_df = pd.concat(dfs)

plt.figure(figsize=(7,6))
sns.lineplot(
    data=plot_df,
    x="Region",
    y="CpG_density",
    hue="Species",
    marker="o",
    linewidth=2
)

plt.ylabel("Mean CpG density (relative)")
plt.xlabel("")
plt.title("Gene body–centric CpG enrichment across millet coding sequences")

plt.tight_layout()
plt.savefig("figures/Figure2_CpG_metagene_density.png", dpi=300)
plt.close()
