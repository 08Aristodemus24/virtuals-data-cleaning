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
import shutil

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

def rename_all(dir: str='<drive name e.g. `C:`>:/Users/<user>/<dir>'):
    """
    
    """

    files = os.listdir(dir)
    for file in files:
        new_file = re.sub(r'[\(\)\s]', "", file)
        source = os.path.join(dir, file)
        dest = os.path.join(dir, new_file)
        os.rename(source, dest)

def copytree(src, dst, symlinks=False, ignore=None):
    """
    
    """
    # lists all the files and folders in directory
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)

        # checks if file is a directory 
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)