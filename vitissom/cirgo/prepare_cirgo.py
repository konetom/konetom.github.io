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
from common import *


def prepare_input():
    newdir("input")
    path = join("..", "revigo", "output")
    for filename in sorted(os.listdir(path)):
        file = join(path, filename)
        try:
            df = pd.read_csv(file, sep="\t", skiprows=4, header=0)
        except:
            df = pd.read_csv(file)
            if df.shape[0] == 0:
                print(f'File "{filename}" is empty, so not processed.')
        else:
            if df.shape[0] == 1:
                df.iloc[0, [1, 3, 6]] = [df.iloc[0, 1]] + \
                    [100] + [df.iloc[0, 1]]
                df.loc[1] = [""] + ["-"] * (df.shape[1] - 2) + [""]
            else:
                df.iloc[:, -1].fillna(df.iloc[:, 1], inplace=True)
            out_filename = filename.replace(".txt", ".tsv")
            df.to_csv(join("input", out_filename), sep=",", index=False)


if __name__ == '__main__':
    main()
