#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare genes from SOM to run gmap.

@author:
    Tomas Konecny

Last modification:
    21.4.2023
"""

import os
import re
import pandas as pd
from shutil import rmtree as rm
from os.path import join
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
        number = int(input("Number: "))
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
        spotlist = str(opts[number])
    except KeyError:
        print("ERROR!!!")
        print("Invalid number! Please select a valid option. Press ENTER and start again.")
        input()
        return get_som_module_data(path)
    if spotlist is None:
        print("ERROR!!!")
        print("Please try it again.")
        input()
        return get_som_module_data(path)
    query = re.compile(f".*{spotlist}").match
    out_path = join(path, "output", "CSV Sheets", "Spot Lists")
    inputs = list(filter(query, os.listdir(out_path)))
    if len(inputs) == 0:
        print("Module data not found. Please, choose different module. [ENTER]")
        input()
        return get_som_module_data(path)
    else:
        print(f'Module "{spotlist}" selected.')
        files = [join(out_path, i) for i in sorted(inputs)]
        return files, spotlist, number


def prepare_input():
    som_path = join("..", "som")
    paths, spot_n, spot_no = get_som_module_data(som_path)
    if "input" in os.listdir():
        rm("input")
    newdir("input")
    for path in paths:
        out_file = join('input', path.split(" ")[-1]).replace(".csv", ".txt")
        df = pd.read_csv(path, sep=",", header=0, usecols=[2], names=["new"])
        df.to_csv(out_file, index=False, header=False)
    return spot_n, spot_no


if __name__ == "__main__":
    prepare_input()
