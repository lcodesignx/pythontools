#!/usr/bin/env python

# word count program

# word dictionary
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

def main():
    word_frequency()

if __name__ == '__main__':
    main()