# -*- coding: utf-8 -*-

import requests
import gzip
import argparse
from utils import *


class GDCDownloader(object):
    def __init__(self, config=None):
        if config is None:
            config = json.load(open("config.json"))
        self.__config = config

    def download_file(self, file_id, end_dir=None):

        if end_dir is None:
            end_dir = self.__config["dir"]

        try:
            print("Downloading file: {}  ...".format(file_id))

            data_endpt = "https://api.gdc.cancer.gov/data/{}".format(file_id)
            response = requests.get(data_endpt)

            unzipped_file = gzip.decompress(response.content)
            check_dir_exsits(end_dir)

            save_b_file(end_dir + "/" + file_id + ".tsv", unzipped_file)

            print("File has been downloaded successfully\n")
        except Exception as err:
            print("Error occurred while downloading and saving file: {} ".format(err))


def get_arg():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file", type=str, required=True,
                      help="Id of the file that has to be downloaded")

    parser.add_argument("-d", "--dir", type=str, default=os.getcwd(),
                      help="The directory, in which file has to be saved")

    options = parser.parse_args()
    return options


def main():
    """Main Function"""
    options = get_arg()
    config = json.load(open("config.json"))
    gdc_downloader = GDCDownloader(config)
    gdc_downloader.download_file(file_id=vars(options)['file'], end_dir=vars(options)['dir'])


if __name__ == '__main__':
    main()
