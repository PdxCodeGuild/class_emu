# cvc_finder.py

import string
input_string = 'abcadeefghijkopq'
vowel_string = 'aoeuiy'
consonant_string = ''
for letter in string.ascii_lowercase:
    if letter not in vowel_string:
        consonant_string += letter

for num in range(1, len(input_string)-1):

    if input_string[num + 1] in consonant_string and input_string[num] in vowel_string and input_string[num-1] in consonant_string:
        print(input_string[num-1:num+2])
