# lab21_count_words_V2.py
'''
** Version 2 **

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

'''
with open('/Users/VapeSwitch/Desktop/class_emu/1 Python/data/apothecary.txt', encoding='utf-8') as f: # opens file from specified location as f
    contents = f.read() # defines variable contents to f and .read allows reading of the file
for punctuation in '''!()-[]{};:'",<>./?@#$%^&*_~\\''': # for loop to iterate over the data to find the punctuations
    contents = contents.replace(punctuation, '')  # replaces each punctuation with ''
contents = contents.lower() # makes all words lowercase
contents = contents.split() # splits the contents into a list by white space NOTE: .split() splits by white space by default
# print(contents)
word_pairs = [] # defines variable word_pairs as an empty list
for i in range(len(contents)-1): # for loop to check the index in the range of the length of contents -1.  -1 is so it doesn't try to go past the end of the list
    t = (contents[i], contents[i+1]) # defines variable t as pair of each index with index + 1
    word_pairs.append(t) # appends the word_pairs list with each iteration
# print(word_pairs)


word_dict = {} # defines variable word_dict as an empty dictionary
for word in word_pairs: # for loop to iterate over each word in contents
    if word not in word_dict: # if statement to determine if the word is not in the dictionary, the below code will run
        word_dict[word] = 1 # if the above is true, will add the word with a value of 1
    word_dict[word] += 1 # if the above statement is false, will add value of 1 to the word for each instance
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
