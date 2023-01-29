# -*- coding: utf-8 -*-

import os
import json
import logging

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
