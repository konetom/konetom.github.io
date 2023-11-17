#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Semantic reduction of set of gene ontology terms in REVIGO.

@author:
    Tomas Konecny

Last modification:
    25.2.2023
"""
import os
import time
from os.path import join
from selenium import webdriver
from urllib import request
from revigo.prepare_revigo import *
from common import *


def retry(d, xpathclick, xpathwait):
    clickx(d, xpathclick)
    try:
        waituntilxpath(
            d, xpathwait)
    except:
        print("Retrying...")
        d.implicitly_wait(1)
        return retry()


def banner_url(n):
    return "/html/body/div[" + str(n) + "]/div[3]/div/button[2]"


def close_banner(d):
    try:
        waituntilxpath(d, banner_url(9), 1)
    except:
        try:
            waituntilxpath(d, banner_url(10), 1)
        except:
            pass


def go():
    opts = set_options()
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    files = [i for i in sorted(os.listdir("input"))]
    for file in files:
        with open(join("input", file), "r") as inp:
            input_content = inp.read()
            if len(input_content) == 0:
                print(f"Skipping empty file: {file}")
                continue
        driver.get("http://revigo.irb.hr/")
        close_banner(driver)
        findid(driver, "txtGOInput", input_content)
        n_go = len(input_content)
        if n_go > 50:
            findidsim(driver, "chkSimilarity0_5")
        elif n_go <= 50 and n_go > 30:
            findidsim(driver, "chkSimilarity0_7")
        else:
            findidsim(driver, "chkSimilarity0_9")
        waituntilid(driver, "ui-id-6")
        x = "/html/body/div[1]/div/form/div/div[4]/div[1]/div[6]/div[1]/p[1]/a[1]"
        time.sleep(1)
        try:
            link = copyxpath(driver, x)
        except Exception:
            time.sleep(5)
        link = copyxpath(driver, x)
        namespaces = ["BP", "MF", "CC"]
        for i in range(3):
            link = link[:-1] + str(i + 1)
            filename = file.replace(".txt", "_" + namespaces[i] + ".txt")
            request.urlretrieve(link, join("output", filename))
    driver.quit()


def run():
    get_in("revigo")
    prepare_input()
    newdir("output")
    go()
    get_out()


if __name__ == "__main__":
    run()
