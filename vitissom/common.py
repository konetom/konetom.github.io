#!/usr/bin/env python3
import os
from os.path import join
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def newdir(foldername, path="."):
    if foldername not in os.listdir(path):
        os.mkdir(foldername)
        print(f'Created "{foldername}" folder in {os.getcwd()}')


def get_in(folder):
    if folder not in os.getcwd() and folder in os.listdir():
        os.chdir(folder)


def get_out():
    os.chdir("..")


def waituntilxpath(driver, xpath, time=60):
    WebDriverWait(driver, time).until(
        EC.element_to_be_clickable((By.XPATH, xpath))).click()


def onlywaituntilxpath(driver, xpath, time=60):
    WebDriverWait(driver, time).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))


def waituntilid(driver, id):
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, id))).click()


def copyxpath(driver, text):
    try:
        e = driver.find_element(By.XPATH, text)
    except Exception as ex:
        print(ex)
        return copyxpath(driver, text)
    return e.get_attribute("href")


def findid(driver, idelem, key):
    e = driver.find_element("id", idelem)
    e.send_keys(key)


def findidsim(driver, idelem):
    e = driver.find_element("id", idelem)
    e.send_keys(Keys.SPACE)
    e.send_keys(Keys.ENTER)


def pressx(driver, elem):
    e = driver.find_element(By.XPATH, elem)
    e.send_keys(Keys.ENTER)


def clickx(driver, elem):
    e = driver.find_element(By.XPATH, elem)
    e.click()


def click_spacex(driver, elem):
    e = driver.find_element(By.XPATH, elem)
    e.send_keys(Keys.SPACE)
    # driver.find_element(By.XPATH, elem).click()


def findx(driver, elem, key):
    e = driver.find_element(By.XPATH, elem)
    e.send_keys(key)


def set_options():
    download = join(os.getcwd(), "output")
    options = Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", download)
    options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
    return options
