# filename: lab15_v2_number_to_phrase_runme.py
'''
Lab 15: Number to Phrase - INTERACTIVE SCRIPT

Convert a given number into its english representation.
For example: 67 becomes 'sixty-seven'.
Handle numbers from 0-99.

Version 2
Handle numbers from 100-999.
'''

from lab15_v2_number_to_phrase_unit_tests import get_word_number2
from lab15_functions import get_integer

while True:
    user_number = get_integer("\nEnter a number between 0 - 999 to convert: ", 999)

    print(get_word_number2(user_number))

    try_again = input("\nDo you want to try again? (yes)(no): ").lower()
    if try_again == "no":
        break
