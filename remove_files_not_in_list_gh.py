'''
Add in the files path and make a csv with the basename of the files to be retained. The extention of the desired files can be added if all be the same.

The process is making the csv into a list based on each element in the first column and then checking to see if the files in the current dir are
present in the list. If they are not then remove.
'''
import os
import csv
import argparse
import sys
import pathlib

data_path = path = "D:\files" # files directory path here
csv_guide = "filenamestokeep.csv" # list of files to keep
csv_path = os.path.join(data_path, csv_guide)
ext = ".tif" #input.your.extention.of.files.to.look.at.as.ext, like .txt
with open(csv_path, 'r') as csvfile:
    good_files = []
    for n in csv.reader(csvfile):
        if len(n) > 0: good_files.append(n[0])
    print(good_files)
    all_files = os.listdir(data_path)
    for filename in all_files:
        if filename.endswith(ext) and filename not in good_files:
            print(filename)
            full_file_path = os.path.join(data_path, filename)
            print("File to delete: {} ".format(filename))
            os.remove(full_file_path)
        else:
           print(f"Ignored -- {filename}")
