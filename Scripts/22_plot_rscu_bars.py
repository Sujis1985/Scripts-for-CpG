import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import glob

genetic_code = {
    "TTT":"Phe", "TTC":"Phe", "TTA":"Leu", "TTG":"Leu",
    "CTT":"Leu", "CTC":"Leu", "CTA":"Leu", "CTG":"Leu",
    "ATT":"Ile", "ATC":"Ile", "ATA":"Ile", "ATG":"Met",
    "GTT":"Val", "GTC":"Val", "GTA":"Val", "GTG":"Val",
    "TCT":"Ser", "TCC":"Ser", "TCA":"Ser", "TCG":"Ser",
    "CCT":"Pro", "CCC":"Pro", "CCA":"Pro", "CCG":"Pro",
    "ACT":"Thr", "ACC":"Thr", "ACA":"Thr", "ACG":"Thr",
    "GCT":"Ala", "GCC":"Ala", "GCA":"Ala", "GCG":"Ala",
    "TAT":"Tyr", "TAC":"Tyr", "CAT":"His", "CAC":"His", 
    "CAA":"Gln", "CAG":"Gln", "AAT":"Asn", "AAC":"Asn", 
    "AAA":"Lys", "AAG":"Lys", "GAT":"Asp", "GAC":"Asp", 
    "GAA":"Glu", "GAG":"Glu", "TGT":"Cys", "TGC":"Cys", 
    "TGG":"Trp", "CGT":"Arg", "CGC":"Arg", "CGA":"Arg", 
    "CGG":"Arg", "AGT":"Ser", "AGC":"Ser", "AGA":"Arg", 
    "AGG":"Arg", "GGT":"Gly", "GGC":"Gly", "GGA":"Gly", "GGG":"Gly"
}

dfs = []
for f in glob.glob("results/*_RSCU_comparison.csv"):
    df = pd.read_csv(f)
    rich_col = [c for c in df.columns if "rich" in c.lower()][0]
    poor_col = [c for c in df.columns if "poor" in c.lower()][0]
    
    # Calculate log2 ratio (adding small constant to avoid log(0))
    df["log2_ratio"] = np.log2((df[rich_col] + 0.01) / (df[poor_col] + 0.01))
    dfs.append(df[["Codon", "log2_ratio"]])

# Average across all 6 species
merged_df = pd.concat(dfs).groupby("Codon", as_index=False).mean()

# Map Amino Acids and CpG status
merged_df["AA"] = merged_df["Codon"].map(genetic_code)
merged_df["is_CpG_codon"] = merged_df["Codon"].str.contains("CG")
merged_df['CpG_status'] = merged_df['is_CpG_codon'].map({True: 'CpG codon', False: 'non-CpG codon'})

# Filter to only show Amino Acids that actually have CpG codons
aa_with_cpg = merged_df[merged_df["is_CpG_codon"] == True]["AA"].unique()
plot_df = merged_df[merged_df["AA"].isin(aa_with_cpg)]

plt.figure(figsize=(10, 6))
sns.barplot(data=plot_df, x='AA', y='log2_ratio', hue='CpG_status', 
            palette={'CpG codon': 'tomato', 'non-CpG codon': 'steelblue'})

plt.title('CpG vs non-CpG codon usage by amino acid\n(all 6 species)', fontsize=14)
plt.ylabel('Mean log₂(RSCU_rich/RSCU_poor)', fontsize=12)
plt.xlabel('Amino acid', fontsize=12)
plt.legend(title='Codon type')
plt.xticks(rotation=0)
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.savefig('figures/Figure8B_AA_CpG_bias.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Figure 8B created")
