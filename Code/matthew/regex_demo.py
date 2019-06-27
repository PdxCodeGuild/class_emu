

import requests
import re
import string

# response = requests.get('https://www.google.com/')
# contents = response.text
# 
# matches = re.findall('#[0-9a-fA-F]+', contents)
# print(matches)


# url = 'http://www.veryabc.cn/movie/uploads/script/Dialog-TheShawshankRedemption.txt'
# url = 'http://www.gutenberg.org/files/1524/1524-0.txt'
url = 'http://www.gutenberg.org/files/2600/2600-0.txt'


response = requests.get(url)
contents = response.text



words = contents.split()
# print(words)

words = [word.lower() for word in words]
words = [word.strip(string.punctuation) for word in words] # apply strip to each word
words = [word for word in words if word != ''] # remove all blanks
short_words = [word for word in words if len(word) < 4]
words = [word.replace('’', '') for word in words]


character_regex = r'[\w\d]'
word_regex = r"[\w\d']+"
sentence_regex = r'[\w\s][\.!\?][\w\s]'

character_count = len(re.findall(character_regex, contents))
word_count = len(re.findall(word_regex, contents))
sentence_count = len(re.findall(sentence_regex, contents))

print(4.71*(character_count/word_count) + 0.5*(word_count/sentence_count) - 21.43)

