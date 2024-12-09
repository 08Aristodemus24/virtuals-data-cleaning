import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import os
import re

def element_exists(driver, by, path:str):
    """
    should .find_element() raise a NoSuchElement or StaleElementReference
    exception return false because the element being searched does not exist
    """
    try:
        driver.find_element(by, path)
    except:
        return False
    return True

def rename_all(dir: str='C:/Users/LARRY/Documents/Scripts/virtuals-internship/Aavegotchi output'):
    """
    
    """

    files = os.listdir(dir)
    for file in files:
        new_file = re.sub(r'[\(\)\s]', "", file)
        source = os.path.join(dir, file)
        dest = os.path.join(dir, new_file)
        os.rename(source, dest)