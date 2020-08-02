#!/usr/local/bin/python

import csv 
import sys

filename = sys.argv[1]

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    with open('state_abbr.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_reader:
            csv_writer.writerow(line[1])
