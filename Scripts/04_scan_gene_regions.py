from Bio import SeqIO
import pandas as pd
import sys

fasta = sys.argv[1]
species = fasta.split("_valid")[0]

rows = []

for record in SeqIO.parse(fasta, "fasta"):
    seq = str(record.seq).upper()
    gene_id = record.id
    length = len(seq)

    bins = {"5prime":0, "middle":0, "3prime":0}

    for i in range(0, length, 3):
        codon = seq[i:i+3]
        if "CG" in codon:
            rel_pos = i / length
            if rel_pos <= 0.33:
                bins["5prime"] += 1
            elif rel_pos <= 0.66:
                bins["middle"] += 1
            else:
                bins["3prime"] += 1

    rows.append([
        gene_id, bins["5prime"], bins["middle"], bins["3prime"]
    ])

df = pd.DataFrame(rows, columns=[
    "GeneID","CpG_5prime","CpG_middle","CpG_3prime"
])

out = f"results/{species}_CpG_positional_distribution.csv"
df.to_csv(out, index=False)

print(f"✅ Positional CpG distribution done for {species}")
