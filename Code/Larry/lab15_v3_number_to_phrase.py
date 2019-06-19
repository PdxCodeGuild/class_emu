# filename: lab15_v3_number_to_phrase.py
'''
Lab 15: Number to Phrase

Version 3 (optional)
Convert a number to roman numerals.

+---+---+----+----+-----+-----+------+------+-------+-------+--------+---------+
| I | V | X  | L  | C   | D   | M    | V̅    | X̅     | C̅     | D̅      | M̅       |
+---+---+----+----+-----+-----+------+------+-------+-------+--------+---------+
| 1 | 5 | 10 | 50 | 100 | 500 | 1000 | 5000 | 10000 | 50000 | 500000 | 1000000 |
+---+---+----+----+-----+-----+------+------+-------+-------+--------+---------+
URL: https://www.britannica.com/topic/Roman-numeral

print(u'V\u0305') => V̅ # (u0305 is the overline)

Example:
| 67 =
| 50+10+5+1+1 =
| L + X+V+I+I =
| LXVII

"Repeating a numeral up to three times represents addition of the number.
For example, III represents 1 + 1 + 1 = 3. Only I, X, C, and M can be repeated; V, L, and D cannot be,
and there is no need to do so."
URL: http://sierra.nmsu.edu/morandi/coursematerials/RomanNumerals.html

"For numbers over 1,000, you put a dash over the top of the Roman Numeral to indicate multiplied by 1,000."
URL: https://www.integers.co/questions-answers/how-is-5001-written-in-roman-numerals.html
'''

# Get a number to convert via user input
def get_integer(prompt_text):
    error_msg = "\nThat's not a number between 1 - 4999. Try again."
    while True:
        try:
            num = int(input(prompt_text))
            if num < 1 or num > 4999:
                print(error_msg)
            else:
                return num
        except ValueError:
            print(error_msg)

while True:
    user_number = get_integer("\nEnter a number between 1 - 4999 to convert: ")

    # Break the big integer into smaller & smaller integers
    thousands   = user_number // 1000
    remainder   = user_number % 1000
    fivehundred = remainder // 500
    remainder   = remainder % 500
    hundreds    = remainder // 100
    remainder   = remainder % 100
    fifty       = remainder // 50
    remainder   = remainder % 50
    tens        = remainder // 10
    remainder   = remainder % 10
    five        = remainder // 5
    remainder   = remainder % 5
    ones        = remainder // 1

    # Convert the integers to the Roman equivalent
    roman_equiv = '' # base value for the output string variable

    if 0 < thousands <= 4:
        roman_equiv += "M" * thousands

    if fivehundred == 1 and hundreds == 4:          # 900
        roman_equiv += "CM"
    elif fivehundred == 1 and 3 >= hundreds >= 1:   # 800,700,600
        roman_equiv += "D" + "C" * hundreds
    elif fivehundred == 1:                          # 500
        roman_equiv += "D"
    elif hundreds == 4:                             # 400
        roman_equiv += "CD"
    elif 3 >= hundreds >= 1:                        # 300,200,100
        roman_equiv += "C" * hundreds

    if fifty == 1 and tens == 4:                    # 90
        roman_equiv += "XC"
    elif fifty == 1 and 3 >= tens >= 1:             # 80,70,60
        roman_equiv += "L" + "X" * tens
    elif fifty == 1:                                # 50
        roman_equiv += "L"
    elif tens == 4:                                 # 40
        roman_equiv += "XL"
    elif 3 >= tens >= 1:                            # 30,20,10
        roman_equiv += "X" * tens

    if five == 1 and ones == 4:                     # 9
        roman_equiv += "IX"
    elif five == 1 and 3 >= ones >= 1:              # 8,7,6
        roman_equiv += "V" + "I" * ones
    elif five == 1:                                 # 5
        roman_equiv += "V"
    elif 1 <= ones <= 3:                            # 3,2,1
        roman_equiv += "I" * ones
    elif ones == 4:                                 # 4
        roman_equiv += "IV"


    print(f"{user_number} => {roman_equiv}")

    try_again = input("\nDo you want to try again? (yes)(no): ").lower()
    if try_again == "no":
        break




    #####################################################

    # if five = 1 and ones = 4                    9
    # elif five = 1 and ones between 3 and 1      8,7,6
    # elif five = 1                               5
    # elif ones = 4                               4
    # elif ones between 3 and 1                   3,2,1

    # if five = 1 and ones = 4                    9
    # elif five = 1                               5
    #     if ones between 3 and 1                 8,7,6
    # elif ones = 4                               4
    # elif ones between 3 and 1                   3,2,1

    #####################################################

    # if fivehundred == 1 and hundreds == 4:        # 900
    #     roman_equiv += "CM"
    # elif fivehundred == 1:                        # 500
    #     roman_equiv += "D"
    #     if 0 < hundreds <= 3:                     # 800,700,600
    #         roman_equiv += "C" * hundreds
    # elif hundreds == 4:                           # 400
    #     roman_equiv += "CD"
    # elif 0 < hundreds <= 3:                       # 300,200,100
    #     roman_equiv += "C" * hundreds

    # if fifty == 1 and tens == 4:                  # 90
    #     roman_equiv += "XC"
    # elif fifty == 1:                              # 50
    #     roman_equiv += "L"
    #     if 0 < tens <= 3:                         # 80,70,60
    #         roman_equiv += "X" * tens
    # elif tens == 4:                               # 40
    #     roman_equiv += "XL"
    # elif 0 < tens <= 3:                           # 30,20,10
    #     roman_equiv += "X" * tens

    # if five == 1 and ones == 4:                   # 9
    #     roman_equiv += "IX"
    # elif five == 1:                               # 5
    #     roman_equiv += "V"
    #     if 3 >= ones >= 1:                        # 8,7,6
    #         roman_equiv += "I" * ones
    # elif ones == 4:                               # 4
    #     roman_equiv += "IV"
    # elif 1 <= ones <= 3:                          # 3,2,1
    #     roman_equiv += "I" * ones
