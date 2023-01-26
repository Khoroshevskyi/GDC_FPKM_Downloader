# -*- coding: utf-8 -*-

import os
import json

'''
Script contains functions that are used in few scrips
'''

def check_dir_exsits(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def open_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


def save_b_file(file_name, content):
    print("Saving file ...")
    file = open(file_name, 'wb')
    file.write(content)
    file.close()


def save_file(data, path_name):
    print("Saving file: {}".format(path_name))
    file_object = open(path_name, "w+")
    file_object.write(data)
    file_object.close()
    print("File was saved successfully")


def open_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        data = file.read()
    return data
