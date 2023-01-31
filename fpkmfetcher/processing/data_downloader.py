# -*- coding: utf-8 -*-

import requests
import argparse
from fpkmfetcher.utils import *
from fpkmfetcher.const import GDC_API_DATA_STR

class GDCDownloader(object):
    def __init__(self, config=None):
        if config is None:
            config = json.load(open("config.json"))
        self.__config = config

    def download_file(self, file_id, end_dir=None):

        if end_dir is None:
            end_dir = self.__config["dir"]

        try:
            file_path = os.path.join(end_dir, f"{file_id}.tsv")
            if not os.path.isfile(file_path):
                print(f"Downloading file: {file_id}  ...")

                data_endpoint = f"{GDC_API_DATA_STR}{file_id}"
                response = requests.get(data_endpoint)

                binary_content = response.content
                check_dir_exists(end_dir)
                save_b_file(file_path, binary_content)
                print("File has been downloaded successfully\n")

        except Exception as err:
            print(f"Error occurred while downloading and saving file: {err}")


def get_arg():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f",
        "--file",
        type=str,
        required=True,
        help="Id of the file that has to be downloaded",
    )

    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        default=os.getcwd(),
        help="The directory, in which file has to be saved",
    )

    options = parser.parse_args()
    return options


def main():
    """Main Function"""
    options = get_arg()
    config = json.load(open("config.json"))
    gdc_downloader = GDCDownloader(config)
    gdc_downloader.download_file(
        file_id=vars(options)["file"], end_dir=vars(options)["dir"]
    )


if __name__ == "__main__":
    main()
