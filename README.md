# GDC data processing scripts
Below you can find information about all scripts used for data finding, formatting and downloading from NHI GDC

All information about data and API can be found in the link below:<br />
https://gdc.cancer.gov/

Each of them has different purpose but configuration of all of them can be found in one common config file [config.json](config.json) 

All scripts were developed for python3.x for Windows users (for other platforms is not verified)


## 1. data_founder.py
Script to find data on the gdc.cancer.gov platform.<br />
Script completely uses config file to find necessary information. You have to specify:
- "primary_site" - "type of tumor" that you want to find (multiple choose is not supported) 
  eg. ["breast"]
- "tumor_stages" - tumor stages that you want to find
- "expand" - which data has to be expand (if there is any)(multiple choose is supported) 
eg. ["diagnoses","files"]
  
- "size" - how many cases has to be found.
- "dir" - directory, in which files have to be saved.

**Example**:
```
python data_founder.py
```

## 2. data_formatter.py

**Example**:
```
python data_formatter.py
```

## 3. data_downloader.py

**Example**:

```
python data_downloader.py
```