# Julien Dhouti
# Started: December 22, 2016
# This script is a class of functions that can be applied to text files.

def clear_file(filename):
    """This will clear the given file in FileInitiate."""
    txt = open(filename, 'w')
    txt.truncate()
    txt.close()

def word_count(filename):
    """Will count the amount of words in the given text file"""
    txt = open(filename, 'r')

    
