#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run SOM with CPM values from the supplementary dataset of Londo et al., 2018.

@author:
    Tomas Konecny

Last modification:
    24.2.2023
"""

import os
from os.path import join, isfile
import re
import sys
import shutil
import datetime
import subprocess
import pandas as pd
from common import *
from som.annotation.annotate import annot_process


def get_input_file_name():
    """User defined input file path."""
    print("Type full path of the input file (XLSX format) \
and press ENTER.")
    input_file = str(input())
    if isfile(input_file) and input_file.endswith(".xlsx"):
        return input_file
    else:
        print("Invalid input. Please try it again.")
        return get_input_file_name()


def preprocess_input(file):
    """Remove header and skip wrong accessions."""
    df = pd.read_excel(file)
    df.columns = ["Gene ID"] + df.columns[1:].values.tolist()
    df.fillna(0, inplace=True)
    if "41438_2018_20_MOESM4_ESM.xlsx" in file:
        swap = list(range(12)) + [51] + list(range(12, 51)) + list(range(52, 60))
        df = df.iloc[:, swap]
        print("Riesling-warm replicate 3 column moved to place of missing replicate 1.")
    return df


def to_replace(item, file):
    """Rename column values."""
    replace_dc = {"CF_": "CabFra_", "Ch_": "Chard_", "Ri_": "Riesl_",
                  "Sa_": "Sangio_", "TF_": "Tocai_", "rep": "",
                  "acclimfreeze": "accfreeze"}
    for key in replace_dc.keys():
        if key in item:
            item = item.replace(key, replace_dc[key])
    if "41438_2018_20_MOESM4_ESM.xlsx" in file:
        item = item[2:] + "_r" + item[0]
    if "Riesl_warm_r3" in item:
        item = item.replace("r3", "r1")
    return item


def check_existing_input():
    input_file = "SOM_input.csv"
    if input_file not in os.listdir("input"):
        input_filename = get_input_file_name()
        clean_df = preprocess_input(input_filename)
        clean_df.columns = [i if i == "Gene ID" else to_replace(i, input_filename) for i in clean_df.columns]
        get_in("annotation")
        annot_process(clean_df)
        get_out()
    input_df = pd.read_csv(join("input", input_file), index_col=[0])
    rows, cols = input_df.shape
    print(f"""
---------------------------------------------------
Input dataset dimension: {rows} genes x {cols} features
---------------------------------------------------
""")


def run():
    get_in("som")
    try:
        check_existing_input()
    except Exception:
        raise Exception("Something went wrong. \
            Please check if the input file path is correct and try it again.")
    else:
        if sys.platform != "linux":
            raise Exception("Please run the R scripts manually.")
        else:
            os.system("chmod +x prepare.R main.R")
            files = [i for i in sorted(os.listdir()) if i.endswith(".R")]
            cwd = os.getcwd()
            logfile = "git.log"
            if logfile not in os.listdir(cwd):
                subprocess.call(join(cwd, files[1]))
                exacttime = datetime.datetime.now()
                with open(join(cwd, logfile), "w") as gitlog:
                    gitlog.write(f"vitisSOM installed on: {exacttime}")
            try:
                subprocess.call(join(cwd, files[0]))
            except Exception as e:
                print(e)
            else:
                outd = "output"
                if outd in os.listdir():
                    shutil.rmtree(outd)
                res = re.findall("SOM[+]{0,9} - Results", ''.join(os.listdir()))
                if len(res) > 0:
                    os.rename(res[-1], outd)
            finally:
                get_out()


if __name__ == "__main__":
    run()
