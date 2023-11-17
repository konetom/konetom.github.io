#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse gene names from GFF3 file.

Usage:
    ./<script-name>.py

Author:
    Tomas Konecny

Last modification:
    19.05.2023 (DD.MM.YYYY)
"""

import os
import re
import numpy as np
import pandas as pd
from os.path import join


def annot_process(som_df):
    if os.getcwd().endswith("som"):
        os.chdir("annotation")
    os.system("chmod +x *.sh")
    os.system("bash *.sh")

    annot_df = pd.read_table("filtered_gene_annotation.gff3", sep="\t", usecols=[8])

    genes = []
    for row in annot_df.values:
        try:
            vitvis = re.findall(r"Vitvi.{8}", row[0])
            aliases = re.findall(r"VIT_.{13}", row[0])
        except Exception:
            pass
        if len(vitvis) != 0 and len(aliases) != 0:
            for alias in aliases:
                genes.append(f"{vitvis[0]},{alias}")

    data = [i.split(",") for i in genes]
    df = pd.DataFrame(data, columns=["new", "old"])
    df.sort_values("new", inplace=True)

    df = df.replace("", None).dropna()
    outfilename = "annotated_genes.csv"
    df.to_csv(outfilename, index=False)

    df = som_df.merge(df, left_on="Gene ID", right_on="old")
    df = df.drop(["old", "Gene ID"], axis=1)
    df.columns = [i.replace("new", "Gene ID") if i == "new" else i for i in df.columns]
    df.drop_duplicates(subset=["Gene ID"], inplace=True)
    df.set_index("Gene ID", inplace=True)
    df = np.log(df + 1)
    df.to_csv(join("..", "input", "SOM_input.csv"))


if __name__ == "__main__":
    pass
