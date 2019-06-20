# filename: lab15_v3_number_to_phrase_runme.py
'''
Lab 15: Number to Phrase - INTERACTIVE SCRIPT

Version 3 (optional)
Convert a number to roman numerals.
'''

from lab15_v3_number_to_phrase_unit_tests import get_roman_numerals
from lab15_functions import get_integer

while True:
    user_number = get_integer("\nEnter a number between 1 - 4999 to convert: ", 4999)

    print(f"{user_number} => {get_roman_numerals(user_number)}")

    try_again = input("\nDo you want to try again? (yes)(no): ").lower()
    if try_again == "no":
        break
