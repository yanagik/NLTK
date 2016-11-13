# NLTK.org/book

# Installation instructions: http://www.nltk.org/install.html

# import nltk
# nltk.download()
# Select book

# From NLTK's book module, load all items.
from nltk.book import *

# Concordance shows every occurrence of a given word, with some context
text1.concordance("monstrous")

# What other words appear in a similar range of contexts?
text1.similar("monstrous")

# Examine contexts shared by two or more words
text2.common_contexts(["monstrous","very"])

# Determine location of a word in the context, or how many words from the beginning it appears
# Note: As of November 13, 2016, the book's example code does not work.
# http://stackoverflow.com/questions/25182140/dispersion-plot-not-working-inspite-of-installing-matplotlib

from nltk.draw.dispersion import dispersion_plot

words=["citizens","democracy","freedom","duties","America"]
dispersion_plot(text4,words)

# Find out the length of a text, in terms of words and punctuation
len(text3)

# len() returns a number of tokens, or a sequence of characters to be treated as a group

# Obtain vocabulary of a text, or the set of tokens used
sorted(set(text3))

len(set(text3))

# Compute lexical richness defined as percentage of unique words
len(set(text3))/len(text3)

# Count how often a word occurs
text3.count("smote")

# Compute percentage of the text taken up by a specific word
100*text4.count('a')/len(text4)

# Exercise: How many times does the word 'lol' appear in text5?
text5.count("lol")

# Exercise: How much is this as a percentage of the total number of words in this text?
100*text5.count("lol")/len(text5)

# Define two functions
def lexical_diversity(text):
    return len(set(text))/len(text)

def percentage(count,total):
    return 100*count/total
