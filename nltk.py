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

# Appending adds a single item to a list
sent1.append("Some")

# Given a word, find the index of when it first occurs
text4.index('awaken')

# Indexes start from 0

# A slice m:n starts at m and ends at n-1

# Omitting m means starting at the beginning; omitting n means going to the end.

# Think of strings as individual words.

# 50 most common words in a text
fdist1=FreqDist(text1)
print(fdist1)
fdist1.most_common(50)

# Cumulative frequency plot
fdist1.plot(50,cumulative=True)

# List of words that occur once only, not to be confused with the set of all words
fdist1.hapaxes()

# For each word in the vocabulary, check whether the length of the word exceeds 15
V=set(text1)
long_words=[w for w in V if len(w)>15]
sorted(long_words)

# The words in the chat corpus that are longer than seven characters and occur more than seven times
fdist5=FreqDist(text5)
sorted(w for w in set(text5) if len(w)>7 and fdist5[w]>7)

# Look at distribution of word lengths in a text
[len(w) for w in text1]
fdist=FreqDist(len(w) for w in text1)
print(fdist)
fdist

#Create a list of the elements in the set of unique words in text7 that contain both a hyphen and the substring "index"
sorted(w for w in set(text7) if '-' in w and 'index' in w)

#Create a list of the elements in the set of unique words in text3 that are initially capitalized and are longer than 10 characters
sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10)

#Create a list of the elements in the set of unique words in sent7 that are not all lowercase
sorted(w for w in set(sent7) if not w.islower())

#Create a list of the elements in the set of unique words in text2 that have either the substring "cie" or the substring "cei"
sorted(t for t in set(text2) if 'cie' in t or 'cei' in t)
