#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Map genes from SOM to BRITE categories.

@author:
    Tomas Konecny

Last modification:
    28.4.2023
"""

import os
import re
import sys
import time
import string
import platform
from os.path import join
import pandas as pd
import seaborn as sns
from bokeh.plotting import figure, output_file, save
from bokeh.io import export_svgs, export_png
from selenium import webdriver
import warnings
from gmap.prepare_gmap import *
from common import *

warnings.filterwarnings("ignore")


def prepare_brite(spot_name, spot_number):
    print(
        """

List of BRITE categories with their IDs:


    Metabolism

          01000  Enzymes
          01001  Protein kinases
          01009  Protein phosphatases and associated proteins
          01002  Peptidases and inhibitors
          01003  Glycosyltransferases
          01005  Lipopolysaccharide biosynthesis proteins
          01011  Peptidoglycan biosynthesis and degradation proteins
          01004  Lipid biosynthesis proteins
          01008  Polyketide biosynthesis proteins
          01006  Prenyltransferases
          01007  Amino acid related enzymes
          00199  Cytochrome P450
          00194  Photosynthesis proteins


    Genetic information processing

          03000  Transcription factors
          03021  Transcription machinery
          03019  Messenger RNA biogenesis
          03041  Spliceosome
          03011  Ribosome
          03009  Ribosome biogenesis
          03016  Transfer RNA biogenesis
          03012  Translation factors
          03110  Chaperones and folding catalysts
          04131  Membrane trafficking
          04121  Ubiquitin system
          03051  Proteasome
          03032  DNA replication proteins
          03036  Chromosome and associated proteins
          03400  DNA repair and recombination proteins
          03029  Mitochondrial biogenesis


    Signaling and cellular processes

          02000  Transporters
          02044  Secretion system
          02042  Bacterial toxins
          03037  Cilium and associated proteins
          04812  Cytoskeleton proteins
          04147  Exosome
          02048  Prokaryotic defense system
          04030  G protein-coupled receptors
          04054  Pattern recognition receptors
          04040  Ion channels
          04031  GTP-binding proteins
          04090  CD molecules
          00535  Proteoglycans
          00536  Glycosaminoglycan binding proteins
          00537  Glycosylphosphatidylinositol (GPI)-anchored proteins
          04091  Lectins
          04990  Domain-containing proteins not elsewhere classified


Specify the BRITE category ID and press ENTER.
(example: type '03036' to use the category 'Chromosome and associated proteins')

"""
    )
    filename = str(input("BRITE ID: "))
    spot_name = spot_name.replace(" ", "_").replace("/", "-").lower()
    if f"{filename}_{spot_number}_{spot_name}.xlsx" in os.listdir("output"):
        return filename

    url_prefix = "https://www.kegg.jp/kegg-bin/download_htext?htext=vvi"
    url_postfix = "&format=htext&filedir=kegg/brite/vvi"

    try:
        print(f"\nRequesting:\n{url_prefix}{filename}{url_postfix}")
        os.system(
            f"wget -O {filename} {url_prefix}{filename}{url_postfix}"
        )
        time.sleep(5)
    except Exception as e:
        print(e)

    if os.path.exists(filename) is False or os.path.getsize(filename) == 0:
        raise FileNotFoundError(
            "Requested file not found or empty. Pleaes try again."
        )
        sys.exit()

    ABC = string.ascii_uppercase
    pattern = r" 1\d{8}"
    name, grp, loc, descr = [], [], [], []
    tail = 0

    with open(filename, "r") as infile:
        lines = infile.read().splitlines()
    os.remove(filename)

    for e, line in enumerate(lines):
        res = re.search(pattern, line)
        if res is None:
            if line[0] in ABC[1:]:
                term = re.sub(fr"^[{ABC}]\s+", "", line)
                head = ABC.index(line[0])
                if tail < head:
                    name.append(term)
                    tail = head
                else:
                    while tail > head:
                        name = name[:-1]
                        tail -= 1
                name = name[:-1]
                name.append(term)
        else:
            grp.append(' - '.join(name))
            res_gr = res.group()[1:]
            loc.append(res_gr)
            descr.append(
                lines[e][lines[e].index(res_gr) + 10:lines[e].index("\t")]
            )

    table = pd.read_csv(join("annotation", "annotated_genes.csv"))

    df = pd.DataFrame(
        {
            "loc": loc,
            "group": grp,
            "description": descr
        }
    )
    df.loc[:, "loc"] = ["LOC" + str(i) for i in df.loc[:, "loc"]]
    print(f"The file contains {df.shape[0]} gene accessions.")
    df = df.merge(table, how="left", on=["loc"])
    df = df.iloc[:, [3, 4, 0, 2, 1]]

    som_path = "input"
    for file in sorted(os.listdir(som_path)):
        spotname = file.replace(".txt", "")
        spot = pd.read_csv(join(som_path, file), header=None, names=["new"])
        spot[spotname] = [1] * spot.shape[0]
        df = df.merge(spot, on="new", how="left")
        print(f"Searching the genes in spot {spotname}.")

    df = df.drop_duplicates("old")
    print(f"Found annotation to {df.shape[0]} genes.")
    df.dropna(subset=df.iloc[:, 5:].columns, how="all", inplace=True)
    df.iloc[:, 5:] = df.iloc[:, 5:].replace("Vitvi.*", 1, regex=True).fillna(0)

    df.to_excel(join("output", f"{filename}_{spot_number}_{spot_name}.xlsx"), index=False)
    return filename


def prepare_map(brite, spot_name, spot_number):
    print(f"Mapping the genes of '{brite}' to the genes of '{spot_name}'.")
    spot_dir = "Spot Lists"
    gps_dir = join("..", "som", "output", "CSV Sheets")
    spot_path = join(gps_dir, spot_dir)
    spot_files = [
        join(spot_path, file) for file in os.listdir(spot_path) if spot_name in file
    ]

    xs, ys, spotval = [], [], []
    for spot_file in spot_files:
        locs = pd.read_csv(spot_file, usecols=[11])
        locs = locs.iloc[:, 0].values.tolist()
        spotval.append([spot_file[-5:].replace(".csv", "")] * len(locs))
        xs.append([int(i.split(" x ")[0]) for i in locs])
        ys.append([int(i.split(" x ")[-1]) for i in locs])
    xs = [i for j in xs for i in j]
    ys = [i for j in ys for i in j]
    spotval = [i for j in spotval for i in j]
    spotdf = pd.DataFrame({"x": xs, "y": ys, "val": spotval})
    spotdf = spotdf.drop_duplicates()

    spotcol = spotdf["val"]
    spotuniq = spotcol.unique()
    spotcp = sns.color_palette("gist_ncar", len(spotuniq), desat=.99).as_hex()
    spotlut = dict(zip(spotuniq, spotcp))
    spotcols = spotcol.map(spotlut)
    spotdf["cols"] = spotcols.values

    gps_file = join(gps_dir, "Gene localization.csv")
    try:
        gps = pd.read_csv(gps_file, usecols=[0, 3])
    except Exception:
        raise FileNotFoundError(
            "File 'Gene localization.csv' not found or corrupted."
        )
        sys.exit()

    gps.columns = ["new", "addr"]
    gps["x"] = [float(i[:i.index("x") - 1]) for i in gps["addr"]]
    gps["y"] = [float(i[i.index("x") + 1:]) for i in gps["addr"]]
    gps.drop("addr", axis=1, inplace=True)

    spot_name = spot_name.replace(" ", "_").replace("/", "-").lower()
    data = pd.read_excel(join("output", f"{brite}_{spot_number}_{spot_name}.xlsx"))
    print(f"In total {data.shape[0]} genes were mapped.")
    data["group"] = [i.split(" - ")[0] for i in data["group"]]
    grps = data.loc[:, "group"].unique()
    print(f"Input data divided into {len(grps)} groups.")
    fname = f"{brite}_{spot_number}"
    return grps, data, gps, spotdf, fname


def map(grps, data, gps, spotdf, fname):
    if platform.system() != "Linux":
        print("This script requires Linux.")
        sys.exit()
    path = "/usr/local/bin/geckodriver"
    if os.path.isfile(path) is False:
        print(
            """
In case of missing geckodriver file, please go to https://github.com/mozilla/geckodriver
and download the version that matches your Firefox browser version.
After downloading, move the geckodriver file to a folder: /usr/local/bin/
"""
        )
        sys.exit()
    driver = webdriver.Firefox(executable_path=path)
    for grp in grps:
        df = data[data.loc[:, "group"] == grp]
        total_genes = df.iloc[:, 5:].to_numpy().sum()
        print(f"Plotting {grp} with {total_genes} genes.")
        df = df.merge(gps, on=["new"])
        df = df.drop_duplicates(subset=["new", "description", "x", "y"])
        df = df.set_index(["new"])

        f = figure(
            tools="tap, pan, wheel_zoom, reset, undo, redo, hover, save",
            active_scroll="wheel_zoom",
            tooltips="@new: @description",
            title=grp,
        )

        f.square(
            x="x",
            y="y",
            fill_color="cols",
            line_color="white",
            line_width=.5,
            size=13,
            source=spotdf,
        )

        f.square(
            x="x",
            y="y",
            fill_color="black",
            line_color="white",
            line_width=.5,
            size=10,
            source=df,
        )

        f.grid.visible = False
        f.xaxis.visible = False
        f.yaxis.visible = False
        f.outline_line_color = None
        f.title.text_font_size = '12pt'
        f.title.text_font_style = "bold"
        f.title.align = "center"
        grp_name = grp.replace(" ", "_").replace("/", "-").lower()
        outfilename = join("output", f"gmap_{fname}_{grp_name}")
        f.output_backend = "svg"
        export_svgs(
            f,
            filename=outfilename + ".svg",
            webdriver=driver,
        )
        output_file(outfilename + ".html")
        save(f)
    driver.close()


def run():
    get_in("gmap")
    newdir("output")
    spot, spot_number = prepare_input()
    br = prepare_brite(spot_name=spot, spot_number=spot_number)
    data = prepare_map(brite=br, spot_name=spot, spot_number=spot_number)
    map(*data)
    print("All gene-map plots are saved in the 'output' folder as HTML and SVG files.")
    get_out()


if __name__ == "__main__":
    run()
