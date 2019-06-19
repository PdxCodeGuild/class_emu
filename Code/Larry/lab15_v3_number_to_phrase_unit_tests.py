# filename: lab15_v3_number_to_phrase_unit_tests.py
'''
Lab 15: Number to Phrase - UNIT TESTS

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

def run_tests(user_number):

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

    return roman_equiv


# try a bunch of numbers as input

input_output = [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (11, "XI"),
    (22, "XXII"),
    (33, "XXXIII"),
    (44, "XLIV"),
    (47, "XLVII"),
    (55, "LV"),
    (67, "LXVII"),
    (73, "LXXIII"),
    (88, "LXXXVIII"),
    (90, "XC"),
    (99, "XCIX"),
    (100, "C"),
    (103, "CIII"),
    (123, "CXXIII"),
    (137, "CXXXVII"),
    (145, "CXLV"),
    (222, "CCXXII"),
    (333, "CCCXXXIII"),
    (455, "CDLV"),
    (555, "DLV"),
    (667, "DCLXVII"),
    (777, "DCCLXXVII"),
    (888, "DCCCLXXXVIII"),
    (990, "CMXC"),
    (999, "CMXCIX"),
    (1034, "MXXXIV"),
    (1072, "MLXXII"),
    (1115, "MCXV"),
    (1444, "MCDXLIV"),
    (1455, "MCDLV"),
    (1555, "MDLV"),
    (1855, "MDCCCLV"),
    (1955, "MCMLV"),
    (1984, "MCMLXXXIV"),
    (2013, "MMXIII"),
    (2559, "MMDLIX"),
    (3499, "MMMCDXCIX"),
    (3984, "MMMCMLXXXIV"),
    (4000, "MMMM"),
    (4001, "MMMMI"),
    (4100, "MMMMC"),
    (4200, "MMMMCC"),
    (4100, "MMMMC"),
    (4499, "MMMMCDXCIX"),
    (4999, "MMMMCMXCIX"),
]

failed_test_count = 0
for i in range(len(input_output)):
    if run_tests(input_output[i][0]) != input_output[i][1]:
        print(f"{input_output[i][0]}: Fail. Expected Result: {input_output[i][1]} ==> Actual result: {run_tests(input_output[i][0])}")
        failed_test_count += 1
if failed_test_count == 0:
        print("All tests passed.")







### Noisy test ### - All passing and non-passing tests are listed
# for i in range(len(input_output)):
#     if run_tests(input_output[i][0]) == input_output[i][1]:
#         print(f"{input_output[i][0]}: Pass")
#     else:
#         print(f"{input_output[i][0]}: Fail. Expected Result: {input_output[i][1]} ==> Actual result: {run_tests(3)}")

### Standalone test ###
# if run_tests(10) == "X":
#     print("10: Pass")
# else:
#     print(f"10: Fail. Expected Result: 'X' ==> Actual result: '{run_tests(10)}'")



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
