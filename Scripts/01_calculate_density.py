from Bio import SeqIO
import pandas as pd
import sys

fasta = sys.argv[1]
species = fasta.split("_valid")[0]

rows = []

for record in SeqIO.parse(fasta, "fasta"):
    seq = str(record.seq).upper()
    gene_id = record.id
    length_kb = len(seq) / 1000

    cpg_dinuc = seq.count("CG")
    density = cpg_dinuc / length_kb if length_kb > 0 else 0

    rows.append([gene_id, cpg_dinuc, density])

df = pd.DataFrame(rows, columns=[
    "GeneID","CpG_dinucleotides","CpG_density_per_kb"
])

out = f"results/{species}_CpG_density.csv"
df.to_csv(out, index=False)

print(f"✅ CpG density calculated for {species}")
