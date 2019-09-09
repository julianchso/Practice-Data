import os
import sys
from tkinter.filedialog import askdirectory

month_folders = [
    "01 January 2019",
    "02 February 2019",
    "03 March 2019",
    "04 April 2019",
    "05 May 2019",
    "06 June 2019",
    "07 July 2019",
    "08 August 2019",
    "09 September 2019",
    "10 October 2019",
    "11 November 2019",
    "12 December 2019"
]

path = askdirectory(title='Select Folder')

for month_folder in month_folders:
    os.makedirs(os.path.join(path, month_folder))
    for day in range(1,32):
        os.makedirs(os.path.join(path, month_folder, "2019" + month_folder[:2] + f"{day:02d}"))
