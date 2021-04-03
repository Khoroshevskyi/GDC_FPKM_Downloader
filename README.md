# GDC data processing scripts
Below you can find information about all scripts used for data finding, formatting and downloading from NHI GDC

All information about data and API can be found in the link below:<br />
https://gdc.cancer.gov/

Each of them has different purpose but configuration of all of them can be found in one common config file [config.json](config.json) 

All scripts were developed for python3.x for Windows users (for other platforms is not verified)


## 1. [data_founder.py](data_founder.py)
Script to find data on the gdc.cancer.gov platform.<br />
Script completely uses [config.json](config.json) to find necessary information. You have to specify:
- "primary_site" - "type of tumor" that you want to find (multiple choose is not supported) 
  e.g. ["breast"]
- "tumor_stages" - tumor stages that you want to find
- "expand" - which data has to be expanded (if there is any)(multiple choose is supported) 
e.g. ["diagnoses","files"]
  
- "size" - how many cases has to be found.
- "dir" - directory, where files have to be saved.
- "join_files" - "True" if you want to join files

data_founder is a main engine for finding, downloading and joining data of gene expression of tumor cells. 
(In the future executing of all scripts has to be transferred to separate script)

**Example**:
```
python data_founder.py
```

## 2. [data_formatter.py](data_formatter.py)

Script to format data that is found in data_founder.py

**Example:**
```
python data_formatter.py -f dir/file
```

## 3. [data_downloader.py](data_downloader.py)

Script to download data by specifying id.
File id is required. Path to save file is optional.

**Example:**

``` 
python data_downloader.py -f 20ae8645-332b-4aa8-a840-2ee2e6e69012 -d directory/of/the/file
```

## 4. [data_joiner.py](data_joiner.py)
Script to merge in appropriate way all files that were saved by data_founder.
<br />
#### Required arguments:
- *-i (--input)* : Path to the input file or directory with FPKM files
- *-o (--output)* : Path to the output file
#### Not Required arguments:
- *-a (--append)* : If you would like to append just one file to existing merged files (e.g. *-a True*) - 
  than you have to specify next arguments:
    - *-s (--stage)* : stage of the tumor (I/II/III/VI)
    - *-c (--caseid)* : id of the case (will be used in output file) <br />
    *Example:*
      ```
      python data_joiner.py -a True -i E:/Przyrod-master/0_master_thesis/data/files/2/stage_1/derevnia22.tsv -o E:/Przyrod-master/0_master_thesis/data/files/2/last_file.csv -s II -c derevnia22 
      ```
- *-m (--method)* : The method that you would like to use to join files. Two method exists:
    - *Append* - This method is better to use if there are 500+ files. It appends new row to existing file. 
      append method takes more time join all the files
    - *Merge* - merging all the files, takes less time than previous method, don't use it if you have low memory!<br />
        *Example:*
      ```
      python data_joiner.py -a True -i E:/Przyrod-master/0_master_thesis/data/files/2 -o E:/Przyrod-master/0_master_thesis/data/files/2/last_file.csv -m Merge
      ```
    
