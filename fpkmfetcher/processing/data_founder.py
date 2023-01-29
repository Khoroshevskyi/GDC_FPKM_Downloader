# -*- coding: utf-8 -*-

import requests
import logging
from fpkmfetcher.processing.data_downloader import GDCDownloader
from fpkmfetcher.processing.data_formatter import DataFormatter
from fpkmfetcher.processing.data_joiner import Joiner
import datetime
import time

from fpkmfetcher.utils import *

_LOGGER = logging.getLogger("fpkmfetcher")


class GDCServer(object):
    def __init__(self, config):

        self.__config = config
        self.file_downloader = GDCDownloader(self.__config)


    def create_params(self, tumor_stage):

        cancer_type = {"op": "in",
                       "content":
                           {"field": "cases.primary_site",
                            "value": self.__config["primary_site"]}
                       }

        stage_value = {"op": "in",
                       "content":
                           {"field": "cases.diagnoses.ajcc_pathologic_stage",
                            "value": tumor_stage}
                       }

        filters = {"op": "and",
                   "content": [cancer_type,
                               stage_value,
                               ]
                   }

        # With a GET request, the filters parameter needs to be converted
        # from a dictionary to JSON-formatted string
        parameters = {
            "filters": json.dumps(filters),
            "expand": self.__config["expand"],
            "format": self.__config["format"],
            "size": self.__config["size"]
        }

        return parameters

    # getting information with expanded diagnoses of one case
    def get_case_by_id(self, case_id, expand=None):
        if expand is None:
            expand = "diagnoses"

        filters = {"op": "and",
                   "content": [{"op": "in",
                                "content":
                                    {"field": "cases.case_id",
                                     "value": case_id}
                                }
                               ]
                   }
        parameters = {
            "filters": json.dumps(filters),
            "expand": [expand],
            # "format": self.__config["format"]
        }
        case_diagnose = requests.get(self.__config["cases_endpt"], params=parameters)
        return case_diagnose.json()

    def get_case_multiple_expands(self, params):
        expand_list = params["expand"]
        params["expand"] = expand_list[0]
        data = requests.get(self.__config["cases_endpt"], params=params).json()

        for expand in expand_list[1:]:
            for case_number in range(len(data["data"]["hits"])):
                diagnose = self.get_case_by_id(data["data"]["hits"][case_number]["case_id"], expand)
                data["data"]["hits"][case_number][expand] = diagnose["data"]["hits"][0][expand]

        return data

    # getting specific cases information with files information and adding diagnoses for it
    def get_case_information(self, tumor_stage):
        try:
            params = self.create_params(tumor_stage)

            if len(params["expand"]) > 1:
                data = self.get_case_multiple_expands(params)
            else:
                data = requests.get(self.__config["cases_endpt"], params=params).json()

            return data

        except Exception as err:
            _LOGGER.info("Error occurred while getting cases information: {}".format(err))

    def save_case_info(self, data, file_name):
        try:
            data_json = json.dumps(data, indent=4)
            file_time = datetime.datetime.now().strftime("_%Y_%m_%d")
            directory = self.__config["dir"] + "/info/"

            check_dir_exsits(directory)

            file_dir_name = directory + "_information_" + file_name + file_time + ".json"

            save_file(data_json, file_dir_name)
            _LOGGER.info("Data has been found successfully\n")
        except Exception as err:
            _LOGGER.info("Error occurred while saving file: {}".format(err))

    # downloading files
    def files_downloader(self, data, stage):
        len_all = len(data["hits"])
        nb_file = 0
        for case in data["hits"]:
            nb_file += 1
            directory = self.__config["dir"] + "/" + stage
            self.file_downloader.download_file(case["fpkm_files"][0]["file_id"], directory)

            _LOGGER.info("Files: {} out of {} have been downloaded".format(nb_file, len_all))
        _LOGGER.info("All files are downloaded! :)")

    # main method of the class, using config file to get all necessary information
    def get(self):
        start = time.time()
        _LOGGER.info("script started")
        for stage in self.__config["tumor_stages"]:
            _LOGGER.info("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-# ")
            _LOGGER.info("Searching files of {} in https://api.gdc.cancer.gov ...".format(stage))
            data = self.get_case_information(self.__config["tumor_stages"][stage])

            file_formatter = DataFormatter(self.__config)
            data = file_formatter.choose_fpkm_data(data)

            self.save_case_info(data, stage)
            self.files_downloader(data, stage)
            # _LOGGER.info(json.dumps(data, indent=4, sort_keys=True))

        if self.__config["join_files"] == "True":
            try:
                _LOGGER.info("File joiner started")
                joiner = Joiner()
                if self.__config["join_method"] == "append": 
                    joiner.join_fpkm_files_append(self.__config["dir"], self.__config["dir"] + "/last_file.csv")
                    _LOGGER.info("append method")
                else:
                    joiner.join_fpkm_files(self.__config["dir"], self.__config["dir"] + "/last_file.csv")
                    _LOGGER.info("merge method")
                _LOGGER.info("Files have been joined successfully")

            except Exception as err:
                _LOGGER.info("Error occurred while joining files: {}".format(err))

        end = time.time() - start
        m, s = divmod(end, 60)
        _LOGGER.info("Time spent: {} min {} sec.".format(int(m), s))


def main():
    """Main Function"""
    config = json.load(open("config.json"))
    gdc_server = GDCServer(config)
    gdc_server.get()


if __name__ == '__main__':
    main()
