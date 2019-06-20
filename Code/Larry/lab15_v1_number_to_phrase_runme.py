# filename: lab15_v1_number_to_phrase_runme.py
'''
Lab 15: Number to Phrase - INTERACTIVE SCRIPT

Convert a given number into its english representation.
For example: 67 becomes 'sixty-seven'.
Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.
| x = 67
| tens_digit = x//10
| ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.
'''

from lab15_v1_number_to_phrase_unit_tests import get_word_number
from lab15_functions import get_integer

while True:
    user_number = get_integer("\nEnter a number between 0 - 99 to convert: ", 99)

    print(get_word_number(user_number))

    try_again = input("\nDo you want to try again? (yes)(no): ").lower()
    if try_again == "no":
        break
