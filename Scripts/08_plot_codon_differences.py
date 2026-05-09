import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob

dfs = []

for f in glob.glob("results/*_Objective2_merged.csv"):
    df = pd.read_csv(f)

    required = ["CpG_class", "ENC", "CAI", "GC3s"]
    if not all(col in df.columns for col in required):
        print(f"Skipping {f} (missing required columns)")
        continue

    # Rename GC3s → GC3 for clarity in plots
    sub = df[required].rename(columns={"GC3s": "GC3"})
    dfs.append(sub)

if not dfs:
    raise ValueError("No valid Objective2 merged files found!")

data = pd.concat(dfs, ignore_index=True)

# Enforce biologically meaningful order
order = ["CpG-poor", "CpG-moderate", "CpG-rich"]
data["CpG_class"] = pd.Categorical(
    data["CpG_class"], categories=order, ordered=True
)

# Plot aesthetics
sns.set(style="whitegrid", font_scale=1.2)
fig, axes = plt.subplots(1, 3, figsize=(14, 5), sharex=True)

metrics = ["ENC", "CAI", "GC3"]
titles = [
    "Effective number of codons (ENC)",
    "Codon Adaptation Index (CAI)",
    "GC content at synonymous 3rd codon positions (GC3)"
]

for ax, metric, title in zip(axes, metrics, titles):
    sns.boxplot(
        data=data,
        x="CpG_class",
        y=metric,
        showfliers=False,
        width=0.6,
        palette="Set2",
        ax=ax
    )

    sns.stripplot(
        data=data,
        x="CpG_class",
        y=metric,
        color="black",
        size=1.5,
        alpha=0.3,
        jitter=0.25,
        ax=ax
    )

    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel(metric)

plt.suptitle(
    "Functional consequences of CpG gene classes on codon bias and translational efficiency",
    fontsize=14,
    y=1.05
)

plt.tight_layout()
plt.savefig("figures/Figure3_Functional_CpG_class_effects.png", dpi=300)
plt.close()
