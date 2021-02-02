"""Count words in file."""


import sys

def word_counts(file):

    poem = open(file)

    word_counts = {}

    for line in poem:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            word = word.split(",.!?-#&()%@*/:$;.""")
            word = word.lower()

            if word in word_counts:
                word_counts[word] += 1
            
            else:
                word_counts[word] = 1

    for key, value in word_counts.items:
        print(key, value)
    
    return word_counts

# get file from the command line
filename = sys.argv[0]

word_counts(filename)

    




def tokenize(filename):
    """Return list of words from file"""

    tokens = []

    with open(filename) as text_file:
        for line in text_file:
            # strip whitespace from the end of the line, and then split it into
            # words (the default argument in both rstrip() and split() is
            # whitespace)
            line = line.rstrip()
            words = line.split()

            for word in words:

                # strip common punctuation off the word:
                word = word.strip("'\",.!?-#$%^&();:_")

                # you could also do this more comprehensively with:
                #   import string
                #   word = word.strip(string.punctuation)

                # lowercase the word so "Kit" and "kit" are counted together
                word = word.lower()

                # add the word to our list of tokens
                tokens.append(word)

    return tokens


def count_words(words):
    """Return dictionary of word: count from list"""

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_words(word_counts):
    """Print words: count from dictionary"""

    for word, count in word_counts.items():
        print(word, count)


# get the filename from the command line
input_filename = sys.argv[1]

# turn the file into a list of lowercased, punctuation-stripped words
tokens = tokenize(input_filename)

# create a dictionary of word counts
word_counts = count_words(tokens)

# print the words and their counts
print_words(word_counts)


##############################################################################
# Alternately, we could use the Counter class from the collections module:

# from collections import Counter

# word_counts = Counter(tokens)
