# Description: This Python script takes a word as input and returns a list of words that rhyme with the input word.
# Using the CMU Pronouncing Dictionary, the script finds words that have the same pronunciation as the input word.
# results are fairly mixed.

import nltk
from nltk.corpus import cmudict
import sys

nltk.download('cmudict')
prondict = cmudict.dict()

def find_rhymes(word):
    if word not in prondict:
        return []
    word_phones = prondict[word][0]
    rhymes = []
    for key in prondict.keys():
        for pron in prondict[key]:
            if pron[-1] == word_phones[-1]:
                rhymes.append(key)
    return rhymes

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rhyme.py <word>")
        sys.exit(1)

    word = sys.argv[1].lower()
    rhymes = find_rhymes(word)
    for rhyme in rhymes:
        print(rhyme)
