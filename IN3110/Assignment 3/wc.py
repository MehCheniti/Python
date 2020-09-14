#!/usr/bin/env python

import sys
import os

def wordCount(fileName):
    """Prints the total number of lines, words and characters in a file along
    with the file name."""

    lines = 0
    words = 0
    characters = 0
    file = open(fileName, "r")

    for i in file:
        lines += 1
        words += len(i.split())
        characters += len(i)

    file.close()
    print("Lines: ", lines, ", words: ", words, ", characters: ", characters,
    ", file name: ", fileName, ".", sep = "")

for i in sys.argv[1:]:
    wordCount(i)
