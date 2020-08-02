#!/usr/local/bin/python

import csv
import sys

filename = sys.argv[1]

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    #next(csv_reader)

    for line in csv_reader:
        print(line)
