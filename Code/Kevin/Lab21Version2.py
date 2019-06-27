import requests
with open(r'C:\Users\WrenJ\Desktop\class_emu\Code\Kevin\pg59797.txt', 'r', encoding='utf-8') as response:
    contents = response.read()
contents = contents.lower()
for puncutation in '!#$%^&*().,;':
    contents = contents.replace(puncutation, ' ')
word_list = contents.split()
word_dict = {}


word_tuples = [] #created an empty list to place tuples in
for i in range(len(word_list)-1): #iterate over the words in word_list
    t = (word_list[i], word_list[i+1]) #create a new tuple based off of word i and word i+1
    word_tuples.append(t) #append t into word_tuples as you loop
print(word_tuples[0])

for words in word_tuples: #loop through every word in the tuple
    if words in word_dict: #if the word is not in the dictionary!
        word_dict[words] += 1 #add the word to the dictionary
    else:
        word_dict[words] = 1 #else leave it alone
print(word_dict)

words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])