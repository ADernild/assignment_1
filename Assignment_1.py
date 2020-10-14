# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:46:10 2020

@author: Alexander Dernild
"""
#%% Importing libraries

import os
import re
import math
import matplotlib.pyplot as plt

#%% 1) Pythagorean theorem

def pythagorean_theorem(a, b, c):
    """

    Parameters
    ----------
    a : TYPE string
        length of a, if ? the length is unknown.
    b : TYPE string
        length of b, if ? the length is unknown.
    c : TYPE string
        length of c, if ? the length is unknown.

    Returns
    -------
    unknown : TYPE float
        the unknown length.

    """
    unknown = 0
    
    if a == "?":
        unknown = math.sqrt(float(c)**2 - float(b)**2)
    elif b == "?":
        unknown = math.sqrt(float(c)**2 - float(a)**2)
    else:
        unknown = math.sqrt(float(a)**2 + float(b)**2)
    return unknown

#%% Taking user input

def use_pythagoras():
    print("Enter the lengths you know and ? (question-mark) for the length you don't know")
    c = input("What is the length of the hypotenuse? ")
    a = input("What is the lenght of one of the sides? ")
    b = input("What is the length of the other side? ")
    print(pythagorean_theorem(a, b, c))

#%% 2) Median value

def median(L):
    """

    Parameters
    ----------
    L : TYPE list
        a list of numbers.

    Returns
    -------
    TYPE float
        the midmost element of the list L or mean of the two midmost elements.
    """
    L.sort()
    middle = len(L)/2
    if len(L) % 2 != 0:
        return L[int(middle - .5)]
    else:
        return ((L[int(middle)] + L[int(middle-1)])/2)

#%% test median

L = [1, 5, 7, 2, 8, 9, 3, 6]

print(median(L))

#%% 3a) Unique list items (removing duplicates from list)

def unique(L):
    """

    Parameters
    ----------
    L : TYPE list
        a list of items.

    Returns
    -------
    unique : TYPE list
        Every unique value in list L.
    """
    unique = []
    for o in L:
        if o not in unique:
            unique.append(o)
    return unique
        
#%% 3b) Unique list items 2 (returning only the unique elements)

def unique2(L):
    """

    Parameters
    ----------
    L : TYPE list
        a list of items.

    Returns
    -------
    unique : TYPE list
        Every unique value in list L that occurs only once.
    """
    unique = []
    for o in L:
        if o in unique:
            unique.remove(o)
        else: 
            unique.append(o)
    return unique

#%% Test unique and unique2

L = ["hey", 0, 5, "hey", 6, 6, 7]

print(unique(L))
print(unique2(L))


#%% 4) Character count

def characters(textfile):
    """
    
    Parameters
    ----------
    textfile : TYPE string
        the file name of the text to be used.

    Prints
    -------
    Each character used along with the count of this character

    """
    characters = {}
    lines = open(textfile).read().split("\n")
    for line in lines:
        for ch in line:
            if ch in characters.keys():
                characters[ch] += 1
            else:
                characters[ch] = 1
    for key in sorted(characters.keys()):
        print(key, " :: ", characters[key])

#%% Test characters

print(characters("raven.txt"))

#%% Helper function load_text

def load_text(path):
    """

    Parameters
    ----------
    path : TYPE string
        path to a text-file.

    Returns
    -------
    lines : TYPE list
        list of lines in text-file.

    """
    file = open(path, "r", encoding = "UTF-8")
    lines = []
    for line in file:
        line = line.lower()
        line = re.sub('[^a-z\'\- ]','', line).strip()
        lines.append(line)
    file.close()
    return lines

#%% 5) Word Frequency

def count(term):
    dir = 'genesis'
    files = sorted(os.listdir(dir))
    frequencies = []
    
    for file in files:
        word_counter = 0
        lines = load_text('genesis/' + file)
        for line in lines:
            words = line.split(" ")
            for word in words:
                if word == term.lower():
                    word_counter += 1
        frequencies.append(word_counter)
    fig = plt.figure(figsize=(15, 10)) 
    plt.plot(list(range(1, len(frequencies) + 1)), frequencies)
    fig.suptitle('Frequency of "' + term + '" in each chapter of genesis', fontsize=25)
    plt.xlabel('Chapters', fontsize=20)
    plt.ylabel('Frequency', fontsize=20)
    fig.savefig('Frequency_plot.jpg')

#%% Test count

count("God")
