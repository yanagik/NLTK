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

#Length of text1
len(text1)

#Unique words in text1
len(set(text1))

#Unique words in text1 after treating words which differ only in capitalization as the same
len(set(word.lower() for word in text1))

#Unique words in text1 after lowercasing only those words that are purely alphabetic
len(set(word.lower() for word in text1 if word.isalpha()))

#Compare to
#Unique words in text1 after including only those words that are lowercased
len(set(word for word in text1 if word.islower()))

#Perhaps it would have been simpler just to count the lowercase-only items, but this gives the wrong answer (why?)
#Answer: If you do it this way, you are including only those words that were already lowercase-only to begin with.

#How many words are there in text2? How many distinct words are there?
len(text2)
len(set(text2))

#Find the collocations in text5.
text5.collocations()

#Consider the following Python expression: len(set(text4)). State the purpose of this expression. Describe the two steps involved in performing this computation.
#The number of unique words in text4. set(text4) returns a list of all the unique words in text4, and len(set(text4)) returns the number of elements in this list.

#Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.
fullsent=sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8
len(set(fullsent))

#Lower case every word in text1. Then return a set of the unique resulting lower-cased words.
sorted(set(w.lower() for w in text1))

#Lower case every word in the set of unique words in text1.
sorted(w.lower() for w in set(text1))

#The second will give a larger value. "The" and "the" are in set(text1), but only "the" is in the set of unique lower-cased words.

#What is the difference between the following two tests: w.isupper() and not w.islower()?
#w.isupper() tests if w contains cased characters and all are uppercase.
#w.islower() tests if w contains cased characters and all are lowercase.
#not w.islower() tests if w doesn't contain cased characters or isn't all lowercase.

#Write the slice expression that extracts the last two words of text2.
text2[-2:]

#Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.
