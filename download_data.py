import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor
import requests
import re
import time 
import shutil

import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from argparse import ArgumentParser

from utilities.utilities import element_exists

def _download_data(driver: webdriver.Chrome, link: str, downloads_path: str, output_dir_name: str):
    """
    args:
        driver - 
        link - 
        download_path - 
        output_dir_name - 
    """

    driver.get(link)
    driver.maximize_window()
    time.sleep(5)

    contribs_btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/button[2]')
    contribs_btn.click()

    # select all div elements first
    list_container = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/div/div[1]')
    divs = list_container.find_elements(By.CSS_SELECTOR, 'div.MuiStack-root')
    divs_to_download = [
        div.find_element(By.CSS_SELECTOR, 'div:first-child > div:first-child') \
        for div in divs if element_exists(div, By.CSS_SELECTOR, 'div:first-child > div:first-child') \
        and bool(re.search(r"dataset#[0-9]{1,}", div.text.lower()))]
    
    outputs = []
    for el in divs_to_download:
        div = el if element_exists(el, By.CSS_SELECTOR, "svg.tabler-icon-download") else None 
        outputs.append(div)

    # remove divs with no svgs as there may be potential
    # repeating divs that have no svgs
    outputs = list(filter(None, set(outputs)))

    # create output directory for datasets/inputs
    # if one does not already exist
    output_dir = f'./{output_dir_name}'
    os.makedirs(output_dir, exist_ok=True)

    # iterate through all divs with clickable svgs
    for div in outputs:
        # extract dataset number from div
        text = re.sub(r"[\n]", " ", div.text.lower())
        dataset_num = re.search(r"dataset#[0-9]+", text)[0]
        print(f"downloading {dataset_num}...")

        # extracting clickable svg
        svg = div.find_element(By.CSS_SELECTOR, "svg.tabler-icon-download")
        svg.click()

        # give 2 second delay so file can be downloaded
        time.sleep(3)

        # get most rececntly downloaded file
        print(os.listdir(downloads_path))
        file_path = max([os.path.join(downloads_path, f) for f in os.listdir(downloads_path)], key=os.path.getctime)
        base_file_name = file_path.split('\\')[-1]
        new_file_name = f"{dataset_num}{base_file_name}"
        new_file_path = os.path.join(downloads_path, new_file_name)
        os.rename(file_path, new_file_path)

        # move downloaded file to current working directory of the script
        relocated_path = os.path.join(output_dir, new_file_name)
        shutil.move(new_file_path, relocated_path)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--link", type=str, help="specifies the link to use to get the datasets")
    parser.add_argument("--downloads_path", type=str, default='C:/Users/LARRY/Downloads', help="path to the downloads folder where datasets will be stored initially")
    parser.add_argument("--output_dir_name", type=str, default="output", help="name of the folder where the newly downloaded datasets will be moved. This folder will be stored relative to this script")
    args = parser.parse_args()

    # define driver
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("prefs", {'profile.default_content_setting_values.automatic_downloads': 1})
    service = ChromeService(executable_path=ChromeDriverManager().install())

    # link where to download data
    link = args.link
    driver = webdriver.Chrome(options=chrome_options, service=service)
    downloads_path = args.downloads_path
    output_dir_name = args.output_dir_name

    # commence download
    _download_data(driver, link, downloads_path, output_dir_name)
    


