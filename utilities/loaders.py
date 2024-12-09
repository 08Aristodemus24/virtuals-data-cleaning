import pandas as pd
import os
import json
import datetime as dt
from dateutil import parser 
import re
from concurrent.futures import ThreadPoolExecutor

def read_json_files(input_dir: str, files: list[str]):
    def helper(file_name):
        with open(f'{input_dir}/{file_name}', 'r') as file:
            data = json.load(file)
            file.close()

        new_name = file_name.replace('.json', '')
        return new_name, data

    # concurrently read and load all .json files
    with ThreadPoolExecutor() as exe:
        jsons = dict(list(exe.map(helper, files)))
    return jsons

def read_txt_files(input_dir: str, files: list[str]):
    def helper(file_name):
        with open(f'{input_dir}/{file_name}', 'r') as file:
            data = file.readlines()
            file.close()

        new_name = file_name.replace('.txt', '')
        return new_name, data

    # concurrently read and load all .json files
    with ThreadPoolExecutor() as exe:
        txts = dict(list(exe.map(helper, files)))
    return txts