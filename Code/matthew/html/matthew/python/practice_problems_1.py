# practice.py

# def is_a(in_letter):
#     if in_letter == 'a':
#         return True
#     return False

import string
import random

# string practice 1
def letter_double(in_string):
    out_string = ''
    # letter_list = list(in_string)
    for letter in in_string:
        # out_string = out_string + letter * 2
        out_string = out_string + letter + letter
    return out_string

# string practice 3
def latest_letter(input_word):
    alpha_number = 0
    for letter in input_word:
        # print(letter)
        if string.ascii_lowercase.index(letter) > alpha_number:
            alpha_number = string.ascii_lowercase.index(letter)
    return string.ascii_lowercase[alpha_number]

# list practice 1
def random_element(input_list):
    return input_list[random.randint(0, len(input_list) - 1)]

# list practice 2
def list_add():
    num_list = []
    while True:
        user_input = input("Enter a number\n:")
        if user_input == 'done':
            break
        elif user_input != 'done':
            try:
                user_input = int(user_input)
                num_list.append(user_input)
            except ValueError:
                continue
    print(num_list)
list_add()