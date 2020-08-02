#!/usr/bin/env python
import sys

# word count program

# word dictionary
filename = sys.argv[1]
word_dict = {}

def word_frequency(filename):
    """function takes a filename as argument and counts the frequency of a word in it"""
    with open(filename) as f:
        data = f.read()
        words = data.split()
        for word in words:
            if word not in word_dict:
                word_dict[word] = 0
            word_dict[word] += 1
    print(word_dict)

def main():
    word_frequency(filename)

if __name__ == '__main__':
    main()
