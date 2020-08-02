#!/usr/local/bin/python 

import csv 
import sys

filename = sys.argv[1]

with open(filename) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
