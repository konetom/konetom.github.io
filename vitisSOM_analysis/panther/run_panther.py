#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gene ontology enrichment analysis in Panther

@author:
    Tomas Konecny

Last modification:
    24.2.2023
"""
import os
import time
import shutil
from os.path import join
from selenium import webdriver
from panther.prepare_panther import *
from common import *


def retry_lists(d):
    try:
        findx(driver, "/html/body/div[2]/form/table/tbody/tr/td/table/tbody/tr[8]/td/select", " GO biological process complete")
    except Exception:
        try:
            findx(d, '//*[contains(text(), "Finished selecting lists")]')
            clickx(d, '//*[contains(text(), "Finished selecting lists")]')
        except Exception:
            return retry_lists(d)


def go():
    files = [join("input", file) for file in sorted(os.listdir("input"))]
    opts = set_options()
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get("http://pantherdb.org/tools/uploadRefFile.jsp")
    findid(driver, "fileData", os.path.abspath("GO_ref.txt"))
    findx(driver, "/html/body/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td/table/tbody/tr/td/select", "Vitis vinifera")
    waituntilxpath(driver, "/html/body/form/table/tbody/tr/td[1]/table/tbody/tr[4]/td/a")
    waituntilxpath(driver, "/html/body/div[2]/form/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr[1]/td[3]/a")
    for e, file in enumerate(files):
        print(f'Processing file: {file[-5:]}')
        if e != 0:
            clickx(driver, "/html/body/div[2]/form[1]/table/tbody/tr/td/table/tbody/tr[6]/td/table/tbody/tr[1]/td[3]/a")
        driver.implicitly_wait(1)
        onlywaituntilxpath(driver, "/html/body/div[2]/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/input")
        findx(driver, "/html/body/div[2]/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/input", os.path.abspath(file))
        onlywaituntilxpath(driver, "/html/body/div[2]/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td/a")
        clickx(driver, "/html/body/div[2]/form/table/tbody/tr/td[1]/table/tbody/tr[3]/td/a")
        if e != 0:
            click_spacex(driver, "/html/body/div[2]/form/table/tbody/tr/td[5]/table/tbody/tr/td/table/tbody/tr[1]/td/input")
        time.sleep(1)
        try:
            clickx(driver, '//*[contains(text(), "Finished selecting lists")]')
        except:
            time.sleep(5)
        clickx(driver, '//*[contains(text(), "Finished selecting lists")]')

        findx(driver, "/html/body/div[2]/form/table/tbody/tr/td/table/tbody/tr[8]/td/select", " GO biological process complete")
        clickx(driver, "/html/body/div[2]/form/table/tbody/tr/td/table/tbody/tr[14]/td/a")
        time.sleep(1)
        clickx(driver, "/html/body/div[2]/form/table/tbody/tr/td/table/tbody/tr[14]/td/a")
        time.sleep(1)
        clickx(driver, "/html/body/div[2]/form/table/tbody/tr/td/table/tbody/tr[14]/td/a")
        onlywaituntilxpath(driver, "/html/body/div[2]/form[2]/a[2]")
        clickx(driver, "/html/body/div[2]/form[2]/a[1]")
        shutil.move(join("output", "analysis.txt"), join("output", file[-5:]))
    driver.close()


def run():
    get_in("panther")
    prepare_input()
    newdir("output")
    go()
    get_out()


if __name__ == "__main__":
    run()
