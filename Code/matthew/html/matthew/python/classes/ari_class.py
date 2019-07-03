

import requests
import re


class AriCalculator:
    def __init__(self, url):
        self.url = url

    def load_text(self):
        response = requests.get(self.url)
        self.text = response.text

    def calculate_ari(self):
        text = self.text
        #using this re.sub, i replace all the surnames and initials and characters that have a period that aren't the end of the the sentence with a space.
        text = re.sub(r'Dr\.|Mr\.|Ms\.|[A-Z]\.|Mrs\.|\.net|\.org|\.com|\.gov|http:|\/|www\.',r'', text)
        text = re.sub(r'\!|\?', r'\.', text)
        #my second re.sub replaces all the special characters with a period as they are ends of sentences, but  it's easier to work with if they are all the same symbol.

        text = text.strip()

        #================================================================
        #Average characters per word
        text_list = text.split()
        total_words = len(text_list)

        #length list will determine the length of every word in the text
        length_list = []
        for i in range(len(text_list)):
            length_list.append(len(text_list[i]))
        #total_characters sums up all the character values in length list
        total_characters = 0
        for i in range(len(length_list)):
            total_characters += length_list[i]
        #average is the total characters divided by total words

        average_cw = total_characters/total_words



        #================================================================
        #Average words per sentence

        #Removes the white space from the text, including \n.  replaces it with ''.
        text = re.sub(r'\s', r'', text)

        #Transforms string into list of strings
        sentence_list = text.split('.')

        #This is a counter for the total number of strings.  the for loop iterates over each indice.  each indicie should be a sentence.  The goal is to find the words per sentence
        total_sentences = 0
        for i in range(len(sentence_list)):
            total_sentences += 1
        words_per_sentence = (total_words/total_sentences)

        #inputing the average characters per word and words per sentence into the ari formula, we can calculate ARI.  the if statement is used to determine if there is a remainder.  if there is a remainder we 'round-up' and then remove the decimal so that the ari can be used as a key in the ari_scale.
        ari = ((4.71*average_cw)+(.5* words_per_sentence) - 21.43)
        if ari % 1 > 0:
            ari += 1
            ari = int(round(ari,0))
        return ari


ari_calculator = AriCalculator('http://www.gutenberg.org/cache/epub/59084/pg59084.txt')
ari_calculator.load_text()
ari = ari_calculator.calculate_ari()

print(ari)
