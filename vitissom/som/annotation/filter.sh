#! /usr/bin/env bash
rm filtered_gene_annotation.gff3
gunzip -kv *.gz
cat *.gff3 | grep "gene" | grep "Vitvi" | grep "VIT_" > filtered_gene_annotation.gff3
