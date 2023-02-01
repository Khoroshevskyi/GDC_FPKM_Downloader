# fpkmfetcher
Program for automatic downloading and integration FPKM data and metadata from [Genomic Data Commons Data Portal](https://portal.gdc.cancer.gov/).

Main purpose of this program is to provide user with friendly user interface
to download files from [GDC](https://portal.gdc.cancer.gov/) that contain FPKM data and 
merge all gene expression values into one dataset for further analysis.
Program provides users with functionality that enables to choose what cancer type and stage 
user is interested in.

----- 
This program as subproject for my master thesis: "The usage of Machine learning techniques
in analysis of transcriptomic profiles of tumor cells" at the Wroclaw University of Environmental and Life Sciences.

All information about data and API that have been used in scripts can be found in the link below:<br />
https://gdc.cancer.gov/

fpkmfetcher is built based on Python3.8+ language.

### How to install this package:
```
pip install 'fpkmfetcher @ git+https://github.com/Khoroshevskyi/fpkmfetcher@master#egg=fpkmfetcher'
```

### How to run program
Run `fpkmfetcher` in command line.

____
Some of the code, functionality and methods can be outdated, as the first version of the program was created in 2020
and API, and structure of GDC, Python are rapidly changing.


