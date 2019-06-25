import requests
with open(r'C:\Users\WrenJ\Desktop\class_emu\Code\Kevin\pg59797.txt', 'r', encoding='utf-8') as response:
    contents = response.read()
contents = contents.lower()
for puncutation in '!#$%^&*().,;':
    contents = contents.replace(puncutation, ' ')
word_list = contents.split()
word_dict = {}

for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])