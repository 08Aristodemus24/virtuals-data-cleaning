import pandas as pd
import os
import json
import datetime as dt
import re

from dateutil import parser 
from concurrent.futures import ThreadPoolExecutor
from docx import Document
from striprtf.striprtf import rtf_to_text



def read_files(input_dir, files):
    """
    
    """
    def helper(file_name: str):
        if file_name.endswith('.json'):
            with open(f'{input_dir}/{file_name}', 'r') as file:
                data = json.load(file)
                file.close()

            new_name = file_name.replace('.json', '')
            return new_name, data

        elif file_name.endswith('.txt'):
            with open(f'{input_dir}/{file_name}', 'r') as file:
                data = file.readlines()
                file.close()

            new_name = file_name.replace('.txt', '')
            return new_name, data

        elif file_name.endswith('.rtf'):
            with open(f'{input_dir}/{file_name}', 'r') as file:
                rtf_data = file.read()
                data = rtf_to_text(rtf_data)
                data = data.split('\n')
                file.close()

            new_name = file_name.replace('.rtf', '')
            return new_name, data

        elif file_name.endswith('.docx'):
            print(file_name)
            path = f'{input_dir}/{file_name}'
            doc = Document(path)
            data = [doc.text for doc in doc.paragraphs]

            new_name = re.sub(r'.docx$', '', file_name)
            return new_name, data
        
        elif file_name.endswith('.csv'):
            df = pd.read_csv(f'{input_dir}/{file_name}')
            new_name = re.sub(r'.csv$', '', file_name)
            return new_name, df
        
        elif file_name.endswith('.xlsx'):
            df = pd.read_excel(f'{input_dir}/{file_name}')
            new_name = re.sub(r'.xlsx$', '', file_name)
            return new_name, df
    
        # concurrently read and load all .json files
    with ThreadPoolExecutor() as exe:
        out = dict(list(exe.map(helper, files)))
    return out


def read_doc_files(input_dir: str, files: list[str]) -> dict[list[dict]]:
    def helper(file_name):
        path = f'{input_dir}/{file_name}'
        doc = Document(path)
        data = [doc.text for doc in doc.paragraphs]

        new_name = re.sub(r'.docx|.rtf$', '', file_name)
        return new_name, data

    # concurrently read and load all .json files
    with ThreadPoolExecutor() as exe:
        docs = dict(list(exe.map(helper, files)))
    return docs



def read_json_files(input_dir: str, files: list[str]) -> dict[list[dict]]:
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



def read_txt_files(input_dir: str, files: list[str]) -> dict[list[str]]: 
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



def read_rtf_files(input_dir: str, files: list[str]) -> dict[list[str]]:
    def helper(file_name):
        with open(f'{input_dir}/{file_name}', 'r') as file:
            rtf_data = file.read()
            data = rtf_to_text(rtf_data)
            data = data.split('\n')
            file.close()

        new_name = file_name.replace('.rtf', '')
        return new_name, data



    # concurrently read and load all .json files
    with ThreadPoolExecutor() as exe:
        rtfs = dict(list(exe.map(helper, files)))
    return rtfs