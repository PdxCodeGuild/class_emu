# filename: lab15_v3_number_to_phrase_runme.py
'''
Lab 15: Number to Phrase - INTERACTIVE SCRIPT

Version 3 (optional)
Convert a number to roman numerals.
'''

from lab15_functions import get_integer
from lab15_functions import try_again
from lab15_v3_number_to_phrase_unit_tests import get_roman_numerals

while True:
    user_number = get_integer("\nEnter a number between 1 - 4999 to convert: ", 4999)

    print(f"{user_number} => {get_roman_numerals(user_number)}")

    if try_again("\nDo you want to try again? (yes)(no): "):
        break
