from Bio import SeqIO
import pandas as pd
import sys

fasta = sys.argv[1]
class_file = sys.argv[2]
target_class = sys.argv[3]   # CpG-rich or CpG-poor
out_fasta = sys.argv[4]

df = pd.read_csv(class_file)
genes = set(df[df["CpG_class"] == target_class]["GeneID"])

records = []
for record in SeqIO.parse(fasta, "fasta"):
    if record.id in genes:
        records.append(record)

SeqIO.write(records, out_fasta, "fasta")
print(f"✅ Extracted {len(records)} sequences for {target_class}")
