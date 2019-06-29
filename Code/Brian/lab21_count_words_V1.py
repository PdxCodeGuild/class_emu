# lab21_count_words_V1.py
'''
Lab 21: Count Words

** Version 1 **

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal.
Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values.
If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
     print(words[i])
'''

with open('/Users/VapeSwitch/Desktop/class_emu/1 Python/data/apothecary.txt', encoding='utf-8') as f: # opens file from specified location as f
    contents = f.read() # defines variable contents to f and .read allows reading of the file
for punctuation in '''!()-[]{};:'",<>./?@#$%^&*_~\\''': # for loop to iterate over the data to find the punctuations
    contents = contents.replace(punctuation, '')  # replaces each punctuation with ''
contents = contents.lower() # makes all words lowercase
contents = contents.split() # splits the contents into a list by white space NOTE: .split() splits by white space by default
# print(contents)
word_dict = {} # defines variable word_dict as an empty dictionary
for word in contents: # for loop to iterate over each word in contents
    if word not in word_dict.keys(): # if statement to determine if the word is not in the dictionary, the below code will run
        word_dict[word] = 1 # if the above is true, will add the word with a value of 1
    word_dict[word] += 1 # if the above statement is false, will add value of 1 to the word for each instance
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
# print(word_dict)
# print(word_dict.items()) # prints the sorted key value pair in the word_dict dictionary
