#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REVIGO input needs to follow one of the formats proposed on their webpage.

To get more details please visit: http://revigo.irb.hr/

@author:
    Tomas Konecny

Last modification:
    25.2.2023
"""

import re
import os
import shutil
from os.path import join
import pandas as pd
from common import *


def prepare_input():
    inp = "input"
    if inp in os.listdir():
        shutil.rmtree(inp)
    newdir(inp)
    panther_path = join("..", "panther", "output")
    for file in sorted(os.listdir(panther_path)):
        fpath = join(panther_path, file)
        c = [0, 4, 6]
        try:
            df = pd.read_table(fpath, sep="\t", skiprows=12, header=None, usecols=c)
        except Exception as e:
            print(e)
            print(f"Empty dataset in file {file} - ommited.")
            continue
        df = df[df.iloc[:, 0].str.contains(":")]
        df.iloc[:, 0] = [re.findall("GO:\d{7}", i)[0] for i in df.iloc[:, 0]]
        df = df[df.iloc[:, 1].str.contains("+", regex=False)].drop(4, axis=1)
        df.to_csv(join("input", file), sep=" ", index=False, header=False)
