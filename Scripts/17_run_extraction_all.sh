#!/bin/bash
mkdir -p results

species_list=(
"Echinochloa_esculenta"
"Eleusine_coracana"
"Panicum_miliaceum"
"Pennisetum_glaucum"
"Setaria_italica"
"Sorghum_bicolor"
)

for sp in "${species_list[@]}"
do
  echo "Processing $sp"

  python scripts/16_extract_sequences.py \
  "${sp}_valid.fasta" \
  "results/${sp}_CpG_gene_classes.csv" \
  CpG-rich \
  "results/${sp}_CpG_rich.fasta"

  python scripts/16_extract_sequences.py \
  "${sp}_valid.fasta" \
  "results/${sp}_CpG_gene_classes.csv" \
  CpG-poor \
  "results/${sp}_CpG_poor.fasta"
done
