#!/bin/python

# Small program to read csv
import csv

filename = '/home/lupera1/Downloads/countries.csv'

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    for line in csv_reader:
        print(line)
