# lab05_random_emoticon_generator_V1.py
import random #import used for random generation/choice of intergers and strings
eyes_list = [':', ';'] #defines a list of eyes
nose_list = ['-', '<'] #defines a list of noses
mouth_list = ['P', 'D'] #defines a list of mouths
eyes = random.choice(eyes_list) #chooses randomly from the list of eyes
nose = random.choice(nose_list) #chooses randomly from the list of noses
mouth = random.choice(mouth_list) #chooses randomly from the list of mouths
print(eyes + nose + mouth) #prints a random eye, nose and mouth to create an emoticon 
