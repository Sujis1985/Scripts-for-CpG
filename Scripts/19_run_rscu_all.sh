#!/bin/bash

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
  echo "Computing RSCU for $sp"

  python scripts/18_calculate_rscu.py \
  "results/${sp}_CpG_rich.fasta" \
  "results/${sp}_CpG_rich_RSCU.csv"

  python scripts/18_calculate_rscu.py \
  "results/${sp}_CpG_poor.fasta" \
  "results/${sp}_CpG_poor_RSCU.csv"
done
