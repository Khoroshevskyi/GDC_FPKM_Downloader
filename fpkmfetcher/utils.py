import os
import json
import logging
import requests
from fpkmfetcher.const import GDC_API_DATA_ENDPOINT

"""
Script contains functions that are used in few scrips
"""

_LOGGER = logging.getLogger("fpkmfetcher")


def check_dir_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def open_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def save_b_file(file_name, content):
    _LOGGER.info("Saving file ...")
    with open(file_name, "wb") as file:
        file.write(content)


def save_file(data, path_name):
    _LOGGER.info("Saving file: {}".format(path_name))
    file_object = open(path_name, "w+")
    file_object.write(data)
    file_object.close()
    _LOGGER.info("File was saved successfully")


def open_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        data = file.read()
    return data


def download_file_from_gdc(file_id, end_dir=None):
    try:
        file_path = os.path.join(end_dir, f"{file_id}.tsv")
        if not os.path.isfile(file_path):
            print(f"Downloading file: {file_id}  ...")

            data_endpoint = f"{GDC_API_DATA_ENDPOINT}{file_id}"
            response = requests.get(data_endpoint)

            binary_content = response.content
            check_dir_exists(end_dir)
            save_b_file(file_path, binary_content)
            print("File has been downloaded successfully\n")

    except Exception as err:
        print(f"Error occurred while downloading and saving file: {err}")
