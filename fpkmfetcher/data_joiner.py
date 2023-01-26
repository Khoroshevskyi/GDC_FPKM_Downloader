# -*- coding: utf-8 -*-

import pandas as pd
import os
import argparse
import time

TUMOR_STAGE = {"I": "stage_1",
               "II": "stage_2",
               "III": "stage_3",
               "VI": "stage_4"}


class Joiner(object):
    def __init__(self):
        print("Welcome to joiner app")

    # opening fpkm file and creating pandas dataframe of it
    @staticmethod
    def open_fpkm_file(case_id, tumor_stage, file_path):

        '''pd.read_csv(nrows=1000, delimiter='\\t')'''
        file_content = pd.read_csv(file_path, header=None, delimiter='\t', names=["gene", case_id])
        file_content.loc[len(file_content.index)] = ["tumor_stage", tumor_stage]

        file_content = file_content.set_index('gene')
        file_content = file_content.sort_values('gene')

        return file_content


    # opening each folder and joining files.
    def join_fpkm_files_append(self, main_dir, output_file):
        global df_merge
        tumor_stage_dict = self.get_stages_file_directories(main_dir)
        first_file = True
        for this_stage in tumor_stage_dict.keys():
            print(this_stage)
            for file_name in tumor_stage_dict[this_stage]:

                file_path = main_dir + "/" + this_stage + "/" + file_name
                if first_file:
                    fpkm_df = self.open_fpkm_file(file_name, this_stage, file_path)
                    self.create_new_file(fpkm_df.T, output_file)
                    first_file = False
                else:
                    new_df = self.open_fpkm_file(file_name, this_stage, file_path)
                    self.add_new_case(new_df.T, output_file)

        print("Finished with success!")

    # opening each folder and joining files. - Old version - if files are not so big use it!!
    def join_fpkm_files(self, main_dir, output_file):

        global df_merge
        tumor_stage_dict = self.get_stages_file_directories(main_dir)
        first_file = True
        for this_stage in tumor_stage_dict.keys():
            print(this_stage)
            for file_name in tumor_stage_dict[this_stage]:

                file_path = main_dir + "/" + this_stage + "/" + file_name
                if first_file:
                    df_merge = self.open_fpkm_file(file_name, this_stage, file_path)
                    first_file = False
                else:
                    new_df = self.open_fpkm_file(file_name, this_stage, file_path)
                    df_merge = pd.merge(df_merge, new_df, on='gene')

        df_merge = df_merge.T
        df_merge.to_csv(output_file, sep='\t')

        print("Finished with success!")

    # creating new output file (or rewriting existing)
    def create_new_file(self, fpkm_df, end_file_path):
        fpkm_df.to_csv(end_file_path, sep='\t', mode='w+')

    # adding new case to the end of the file
    def add_new_case(self, fpkm_df, end_file_path):
        try:
            fpkm_df.to_csv(end_file_path, mode='a', header=False, sep="\t")
        except Exception as err:
            print(f"Error occurred: {err}")

    # opening and adding new case to existing file
    def add_new_expression(self, case_id, tumor_stage, expression_file, end_file):
        dd = self.open_fpkm_file(case_id, tumor_stage,expression_file)
        self.add_new_case(dd.T, end_file)

    # getting list of files that are in the directory
    @staticmethod
    def get_stages_file_directories(main_dir):
        directory_contents = os.listdir(main_dir)
        files_dict = {}
        for one_stage_folder in directory_contents:
            if len(one_stage_folder) > 5:
                if one_stage_folder[0:5] == "stage":
                    files_dict[one_stage_folder] = os.listdir(main_dir + "/" + one_stage_folder) # self.list_full_paths(main_dir + "/" + one_stage_folder)

        return files_dict


# The function for getting arguments
def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True,
                        help="Path to the input file (E:/Przyrod-master/0_master_thesis/data/files/2/a23fv.tsv)"
                             " or path to the directory with files")

    parser.add_argument("-o", "--output", type=str, required=True,
                        help="Path to the output file (E:/Przyrod-master/0_master_thesis/data/files/2/last_file.csv)")


    parser.add_argument("-a", "--append", type=str, required=False, default='False',
                        help="Append one file to existing output file (You have to specify input file): True/False")

    parser.add_argument("-m", "--method", type=str, required=False, default='Merge',
                        help="While creating new dataset, you can specify method: Append/Merge - depends on dataset and"
                             " RAM")

    parser.add_argument("-s", "--stage", type=str, required=False, default='I',
                        help="Specify stage of tumor: I/II/III/IV")

    parser.add_argument("-c", "--caseid", type=str, required=False, default='Unknown',
                        help="Specify case id")

    return parser.parse_args()

def main_arguments():
    """Main Function"""
    options = get_arg()
    options = vars(options)

    joiner = Joiner()
    if options['append'].lower() in ['true', 't']:
        joiner.add_new_expression(options['caseid'], TUMOR_STAGE[options['stage']], options['input'], options['output'])
    else:
        if options["method"].lower() == "append":
            joiner.join_fpkm_files_append(options['input'], options['output'])
        else:
            joiner.join_fpkm_files(options['input'], options['output'])




def main():
    """Main Function"""
    joiner = Joiner()

    #joiner.join_fpkm_files_append("E:/Przyrod-master/0_master_thesis/data/files/2",
    #                        "E:/Przyrod-master/0_master_thesis/data/files/2/last_file.csv")

    joiner.join_fpkm_files("E:/Przyrod-master/0_master_thesis/data/files/2",
                           "E:/Przyrod-master/0_master_thesis/data/files/2/last_file.csv")



if __name__ == '__main__':
    start = time.time()
    #main()
    main_arguments()
    end = time.time() - start
    m, s = divmod(end, 60)
    print("Time spent: {} min {} sec.".format(int(m), s))
