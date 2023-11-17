#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vine functional genomics analysis pipeline

@author:
    Tomas Konecny

Last modification:
    26.2.2023
"""

import sys
import argparse
from argparse import RawTextHelpFormatter
from som.run_som import run as s
from gmap.run_gmap import run as g
from panther.run_panther import run as p
from revigo.run_revigo import run as r
from cirgo.run_cirgo import run as c


def cli():
    p = argparse.ArgumentParser(
        prog="vitisSOM analysis pipeline",
        description="""
         __________________________________________
        |                                          |
        |  vitisSOM => Panther => REVIGO => CirGO  |
        |__________________________________________|""",
        epilog="""

EXAMPLES:
1) Run the whole pipeline:
./vitissom.py -m a

2) Run only SOM analysis:
./vitissom.py -m s



created by:
    Tomas Konecny (tomas.konecny@abi.am)
    Armenian Bioinformatics Institute
""",
        formatter_class=RawTextHelpFormatter)
    p.add_argument("-m", default="a", choices=["a", "s", "g", "p", "r", "c"],
                   type=str, help="""MODES:
a - run all [default option]
s - vitisSOM (Vitis vinifera transcriptomic data analysis by Self Organizing Maps)
g - gmap (Map SOM genes on BRITE category of KEGG database)
p - PANTHER (GO enrichment of output datasets from vitisSOM)
r - REVIGO (Semantic similarity reduction of enriched GO sets from PANTHER)
c - CirGO (Visualization of GO sets from REVIGO)
""")
    if len(sys.argv) == 1:
        p.print_help(sys.stderr)
        sys.exit(1)
    mode = p.parse_args().m
    return mode


def run():
    mode = cli()
    if mode == "a":
        s()
        g()
        p()
        r()
        c()
    elif mode == "s":
        s()
    elif mode == "g":
        g()
    elif mode == "p":
        p()
    elif mode == "r":
        r()
    elif mode == "c":
        c()


if __name__ == "__main__":
    run()
