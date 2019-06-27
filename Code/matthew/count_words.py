


import requests

response = requests.get('http://www.gutenberg.org/cache/epub/59797/pg59797.txt')
contents = response.text
print(contents)

with open(r'..\..\1 Python\data\apothecary.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
with open(r'C:\Users\flux\programs\class_emu\1 Python\data\apothecary.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

print(contents.split()) # split on whitespace



text = '!#_hello!world!__'
text.strip('!#_') # hello!world
for punctuation in '!#$%^&*()':
    text = text.replace(punctuation, '')



words = ['hello', 'world', 'apple', 'world', 'banana']
# loop over words
# if the word is in the dictionary, increment the count
# if the word is not in the dictionary, add it with value of 1
counts = {}
counts = {'hello': 1}
counts = {'hello': 1, 'world': 1}
counts = {'hello': 1, 'world': 1, 'apple': 1}
counts = {'hello': 1, 'world': 2, 'apple': 1}
counts = {'hello': 1, 'world': 2, 'apple': 1, 'banana': 1}


