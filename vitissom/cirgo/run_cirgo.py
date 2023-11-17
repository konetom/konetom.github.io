#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process output of REVIGO into input for CirGO

@author:
    Tomas Konecny

Last modification:
    26.2.2023
"""

import os
from os.path import join
import pandas as pd
import seaborn
from cirgo.prepare_cirgo import *
from common import *


def draw():
    in_path = "input"
    out_path = "output"
    newdir(out_path)
    files = [i for i in sorted(os.listdir(in_path)) if ".tsv" in i]
    for file in files:
        in_filename = join(in_path, file)
        out_filename = join(out_path, file).replace(".tsv", ".pdf")
        io = f" -inputFile {in_filename} -outputFile {out_filename}"
        if os.stat(in_filename).st_size != 0:
            name = file[0]
            legend = f"Proportion of GO groups (spot {name})"
            specs = f' -fontSize 10 -leg "{legend}"'
            os.system("python3 " + join("tool", "CirGO.py") + io + specs)


def run():
    get_in("cirgo")
    prepare_input()
    draw()
    get_out()


if __name__ == '__main__':
    run()
