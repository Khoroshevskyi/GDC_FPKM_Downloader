# -*- coding: utf-8 -*-

from fpkmfetcher.utils import *
import argparse


class DataFormatter(object):
    def __init__(self, config):

        self.__config = config
        self.data_new = {"hits": []}

    def add_case_to_dataset(self, case):
        case_data = {"case_id": case["case_id"],
                     "primary_site": case["primary_site"],
                     "created_datetime": case["created_datetime"],
                     "diagnoses": case["diagnoses"],
                     "diagnosis_ids": case["diagnosis_ids"],
                     "disease_type": case["disease_type"],
                     "fpkm_files": []}

        self.data_new["hits"].append(case_data)

    def choose_fpkm_data(self, data):
        print("Correcting data ....")
        for case in data["data"]["hits"]:
            self.add_case_to_dataset(case)
            is_empty = True
            for file in case["files"]:
                if file["file_name"][-11:].lower() == "fpkm.txt.gz" and file["acl"] == ["open"]:
                    is_empty = False
                    self.data_new["hits"][-1]["fpkm_files"].append(file)
            if is_empty:
                self.data_new["hits"].pop()
        print("Data has been corrected successfully!")
        return self.data_new


def main():
    """Main Function"""
    config = json.load(open("config.json"))
    formtatter = DataFormatter(config)

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, required=True,
                        help="Id of the file that has to be formatted")
    options = parser.parse_args()

    file = open_json_file(file_path=vars(options)['file'])
    data = open_json_file(file)
    formtatter.choose_fpkm_data(data)


if __name__ == '__main__':
    main()
