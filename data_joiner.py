import pandas as pd
import os
import argparse
import time


class Joiner(object):
    def __init__(self):
        print("Welcome to joiner app")

    @staticmethod
    def open_fpkm_file(file_dir, tumor_stage, file_name):
        file_dir = file_dir + "/" + tumor_stage + "/" + file_name

        '''pd.read_csv(nrows=1000, delimiter='\\t')'''
        file_content = pd.read_csv(file_dir, header=None, delimiter='\t', names=["gen", file_name])
        file_content.loc[len(file_content.index)] = ["tumor_stage", tumor_stage]
        file_content.loc[len(file_content.index)] = ["file_name", file_name]
        file_content = file_content.set_index('gen')
        return file_content
        # .T -- to transpose our dataset

    def join_fpkm_files(self, main_dir, output_file):

        global df_merge
        tumor_stage_dict = self.get_stages_file_directories(main_dir)
        first_file = True
        for this_stage in tumor_stage_dict.keys():
            print(this_stage)
            for file_name in tumor_stage_dict[this_stage]:
                # self.sort_files(main_dir + "/" + this_stage + "/" + file_name)

                if first_file:
                    df_merge = self.open_fpkm_file(main_dir, this_stage, file_name)
                    first_file = False
                else:
                    new_df = self.open_fpkm_file(main_dir, this_stage, file_name)
                    df_merge = pd.merge(df_merge, new_df, on='gen')

        df_merge = df_merge.T

        df_merge.to_csv(output_file, sep='\t')

        print("Finished with success!")

    @staticmethod
    def sort_files(file_dir):
        file_content = pd.read_csv(file_dir, header=None, delimiter='\t', names=["gen", "expression"])
        file_content = file_content.sort_values('gen')
        file_content.to_csv(file_dir, sep='\t', header=False)

    # we are not using it
    @staticmethod
    def list_full_paths(directory):
        return [os.path.join(directory, file) for file in os.listdir(directory)]

    @staticmethod
    def get_stages_file_directories(main_dir):
        directory_contents = os.listdir(main_dir)
        files_dict = {}
        for one_stage_folder in directory_contents:
            if len(one_stage_folder) > 5:
                if one_stage_folder[0:5] == "stage":
                    files_dict[one_stage_folder] = os.listdir(main_dir + "/" + one_stage_folder)#self.list_full_paths(main_dir + "/" + one_stage_folder)

        return files_dict


def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, required=True,
                        help="Directory of the folders this files")
    parser.add_argument("-o", "--output", type=str, required=True,
                        help="Name of the file with directory, where output file has to be saved")
    return parser.parse_args()


def main():
    """Main Function"""
    joiner = Joiner()
    # options = get_arg()

    start = time.time()
    joiner.join_fpkm_files("E:/Przyrod-master/0_master_thesis/data/files",
                           "E:/Przyrod-master/0_master_thesis/data/files/last_file.csv")

    end = time.time() - start
    m, s = divmod(end, 60)
    print("Time spent: {} min {} sec.".format(int(m), s))


if __name__ == '__main__':
    main()
