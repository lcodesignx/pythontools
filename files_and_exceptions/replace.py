#!/usr/local/bin/python

filename = 'sample.txt'

with open(filename) as f:
    contents = f.readlines()
    for line in contents:
        print(line.replace('to', 'PYTHON').rstrip())
