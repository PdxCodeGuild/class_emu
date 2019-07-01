# filename: lab15_v3_number_to_phrase_unit_tests.py
'''
Lab 15: Number to Phrase - FUNCTION w/ UNIT TESTS

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

def get_roman_numerals(user_number):

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
    elif ones == 4:                                 # 4
        roman_equiv += "IV"
    elif 1 <= ones <= 3:                            # 3,2,1
        roman_equiv += "I" * ones

    return roman_equiv

###########################################################
### UNIT TESTS ###
###########################################################

# Check (at least) one number from every if/elif conditional
if __name__ == '__main__':

    test_data = [
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
        (12, "XII"),
        (13, "XIII"),
        (14, "XIV"),
        (15, "XV"),
        (16, "XVI"),
        (17, "XVII"),
        (18, "XVIII"),
        (19, "XIX"),
        (20, "XX"),
        (21, "XXI"),
        (22, "XXII"),
        (23, "XXIII"),
        (24, "XXIV"),
        (30, "XXX"),
        (33, "XXXIII"),
        (40, "XL"),
        (44, "XLIV"),
        (47, "XLVII"),
        (50, "L"),
        (55, "LV"),
        (60, "LX"),
        (67, "LXVII"),
        (70, "LXX"),
        (73, "LXXIII"),
        (80, "LXXX"),
        (88, "LXXXVIII"),
        (90, "XC"),
        (99, "XCIX"),
        (100, "C"),
        (101, "CI"),
        (102, "CII"),
        (103, "CIII"),
        (123, "CXXIII"),
        (137, "CXXXVII"),
        (145, "CXLV"),
        (200, "CC"),
        (222, "CCXXII"),
        (300, "CCC"),
        (333, "CCCXXXIII"),
        (400, "CD"),
        (455, "CDLV"),
        (500, "D"),
        (555, "DLV"),
        (600, "DC"),
        (667, "DCLXVII"),
        (700, "DCC"),
        (777, "DCCLXXVII"),
        (800, "DCCC"),
        (888, "DCCCLXXXVIII"),
        (900, "CM"),
        (990, "CMXC"),
        (999, "CMXCIX"),
        (1000, "M"),
        (1001, "MI"),
        (1002, "MII"),
        (1003, "MIII"),
        (1034, "MXXXIV"),
        (1072, "MLXXII"),
        (1115, "MCXV"),
        (1444, "MCDXLIV"),
        (1455, "MCDLV"),
        (1555, "MDLV"),
        (1855, "MDCCCLV"),
        (1955, "MCMLV"),
        (1984, "MCMLXXXIV"),
        (1900, "MCM"),
        (2000, "MM"),
        (2001, "MMI"),
        (2002, "MMII"),
        (2013, "MMXIII"),
        (2100, "MMC"),
        (2559, "MMDLIX"),
        (3000, "MMM"),
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

    from lab15_functions import run_tests

    print(run_tests(test_data, get_roman_numerals))
