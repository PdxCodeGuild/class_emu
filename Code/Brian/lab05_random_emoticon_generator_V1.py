# lab05_random_emoticon_generator_V1.py
'''
Lab 5: Random Emoticon Generator

** Version 1 **

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.
Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)
Example output:

:-P
'''
import random #import used for random generation/choice of intergers and strings
eyes_list = [':', ';'] #defines a list of eyes
nose_list = ['-', '<'] #defines a list of noses
mouth_list = ['P', 'D'] #defines a list of mouths
eyes = random.choice(eyes_list) #chooses randomly from the list of eyes
nose = random.choice(nose_list) #chooses randomly from the list of noses
mouth = random.choice(mouth_list) #chooses randomly from the list of mouths
print(eyes + nose + mouth) #prints a random eye, nose and mouth to create an emoticon
