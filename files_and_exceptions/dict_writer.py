#!/usr/local/bin/python 

import csv
import sys

filename = sys.argv[1]

with open(filename) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_states.csv', 'w') as new_file:
        fieldnames = ['State', 'Abbreviation']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
