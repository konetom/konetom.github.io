#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Panther accepts vitis vinifera genes annotated in v2 format, not in v3.

@author:
    Tomas Konecny

Last modification:
    24.2.2023
"""

import re
import os
from os.path import join
import pandas as pd
from common import newdir


def get_som_module_data(path):
    """User defined SOM module."""
    print("""
\t1) Correlation Cluster
\t2) D-Cluster
\t3) Group Overexpression Spots
\t4) K-Means Cluster
\t5) Overexpression Spots
\t6) Underexpression Spots

Select one of the options, type the number and press ENTER.""")
    try:
        number = int(input())
    except ValueError:
        print("ERROR!!!")
        print("An integer number has to be selected. Press ENTER and start again.")
        input()
        return get_som_module_data(path)
    opts = {
        1: "Correlation Cluster",
        2: "D-Cluster",
        3: "Group Overexpression Spots",
        4: "K-Means Cluster",
        5: "Overexpression Spots",
        6: "Underexpression Spots"
    }
    try:
        spotlist = opts[number]
    except KeyError:
        print("ERROR!!!")
        print("Invalid number! Please select a valid option. Press ENTER and start again.")
        input()
        return get_som_module_data(path)
    query = re.compile(f".*{spotlist}").match
    out_path = join(path, "output", "CSV Sheets", "Spot Lists")
    inputs = list(filter(query, os.listdir(out_path)))
    if len(inputs) == 0:
        print("Module not found. Please, choose different module. [ENTER]")
        input()
        get_som_module_data(path)
    else:
        print(f'Module "{spotlist}" selected.')
        files = [join(out_path, i) for i in sorted(inputs)]
        return files


def prepare_input():
    som_path = join("..", "som")
    input_genes = join(som_path, "annotation", "annotated_genes.csv")
    ids = pd.read_csv(input_genes, sep=",", header=0, names=["new", "old"])
    ids.loc[:, "old"].to_csv("GO_ref.txt", index=False, header=False)
    paths = get_som_module_data(som_path)
    newdir("input")
    # newdir("new_input")
    for path in paths:
        out_file = join('input', path.split(" ")[-1]).replace(".csv", ".txt")
        df = pd.read_csv(path, sep=",", header=0, usecols=[2], names=["new"])
        df = df.merge(ids, on=["new"])
        old_df = df.loc[:, "old"]
        old_df.to_csv(out_file, index=False, header=False)
        # new_df = df.loc[:, "new"]
        # new_df.to_csv(out_file.replace("input", "new_input"), index=False, header=False)


if __name__ == "__main__":
    prepare_input()
