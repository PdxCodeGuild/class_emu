# cvc_finder.py


import string
input_string = 'abcadeefghijkopq'
vowel_string = 'aeiouy'
consonant_string = ''

for letter in string.ascii_lowercase:
    if letter not in vowel_string:
        consonant_string += letter
        print(consonant_string)
print(len(input_string))
