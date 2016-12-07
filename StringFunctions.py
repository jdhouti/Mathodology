# Julien Dhouti
# Started: December 6, 2016
# This script is a class of functions that can be applied on given strings.
# All functions applied to lists are pulled directly from the ListFunctions library
# written by the author of this document.

import ListFunctions as lf

def string_length(s):
    """This method counts the amount of characters a given string has."""
    # convert string to a list
    string = list(s)
    length = 0

    # Important to note that we could simply apply this principle by returning
    # the len of the string in list format but this is easier to visualize.
    for i in range(1, lf.list_len(string) + 1):
        length += 1

    return length

def string_reverse(s):
    """This function will reverse any given string."""
    # we must first convert the given string into a list.
    # and create the new String that we will return.
    string = list(s)
    newString = ""

    for i in range(lf.list_len(string)):
        # -(i + 1) represents the incrementation of the index, i, in reverse order
        newString = newString + string[-(i + 1)]

    return newString

def find_vowels(s):
    """This function will find all of the vowels in a given string."""
    # conver the given string into a list
    string = list(s)
    vowelList = []

    for i in string:
        if i in vowels:
            vowelList.append(i)

    return vowelListS

def find_nums(s):
    """This function will find all of the numbers in a given list."""
    string = list(s)
    numberList = []

    for i in string:
        if i not in letters:
            # to prevent numberList from being filled with doubles.
            if i not in numberList:
                numberList.append(i)

    return numberList

def check_nums(s):
    """Check if a given string has any numbers."""
    string = list(s)

    for i in string:
        if i.lower() not in letters:
            return True

    return False

def piglatin(s):


# tell script which chars are vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# tell script what the letters of the alphabet are
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
