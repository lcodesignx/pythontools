#!/usr/local/bin/python

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
