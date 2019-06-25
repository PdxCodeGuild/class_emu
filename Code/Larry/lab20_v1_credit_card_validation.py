# filename: lab20_v1_credit_card_validation.py
'''
Lab 20: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
e.g. credit_card_number = 4556737586899855
+---------------------------------------------------------------------------------------------+
| Steps                                                | Data                                 |
+------------------------------------------------------+--------------------------------------+
| 1. Convert the input string into a list of ints      | 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5      |
| 2. Slice off the last digit. That is the check digit | 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5        |
| 3. Reverse the digits.                               | 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4        |
| 4. Double every other element in the reversed list   | 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8 |
| 5. Subtract nine from numbers over nine              | 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8        |
| 6. Sum all values                                    | 85                                   |
| 7. Take the second digit of that sum                 | 5                                    |
+------------------------------------------------------+--------------------------------------+
| Result: If that matches the check digit, the whole card number is valid.                    |
+---------------------------------------------------------------------------------------------+
'''
import sys # for using sys.argv e.g. $python3 this_file.py run_tests

def validate_credit_card(cc_number):
    numbers = list(cc_number)                    # Convert the input string into a list of ints
    check_digit = numbers.pop()                  # Slice off the last digit. That is the check digit.

    counter = 0                                  #
    numbers_rev = []                             #
    while counter < len(numbers):                #
        numbers_rev.append(numbers[-1-counter])  # Reverse the digits.
        counter += 1                             #

    for i in range(0, len(numbers_rev), 2):      #
        numbers_rev[i] = int(numbers_rev[i]) * 2 # Double every other element in the reversed list.

    for i in range(len(numbers_rev)):            #
        numbers_rev[i] = int(numbers_rev[i])     #
        if numbers_rev[i] > 9:                   #
            numbers_rev[i] = numbers_rev[i] - 9  # Subtract nine from numbers over nine.

    sum = 0
    for number in numbers_rev:                   #
        sum += number                            # Sum all values.

    sum = str(sum)                               #
    if check_digit == sum[1]:                    # If second digit of that sum matches the check digit, ...
        return True                              # ... the whole card number is valid.
    else:
        return False

if len(sys.argv) == 1: # only execute these lines when 'run_tests' is not passed
    # Get user input
    credit_card_number = input("\nEnter a credit card number: ") # Get input, e.g. "4556737586899855"

    # Print the result
    result = validate_credit_card(credit_card_number)
    if result:
        print(f"\n{result}: This is a valid credit card number.\n")
    else:
        print(f"\n{result}: This is not a valid credit card number.\n")

###########################################################
### UNIT TESTS ###
###########################################################

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if len(sys.argv) > 1:
    if sys.argv[1] == 'run_tests':  # 1 first argument after the program name, e.g. py filename.py run_tests

        # source: https://www.getcreditcardnumbers.com/credit-card-generator
        test_data = [
            (1, "4556737586899855", True),   # Lab 20 example
            (2, "4556737586899856", False),  # Lab 20 with check_digit+1
            (3, "378282246310005", True),    # American Express
            (4, "371449635398431", False),   # American Express
            (5, "370132601027215", True),    # American Express
            (6, "374375341030025", True),    # American Express
            (7, "378734493671000", True),    # American Express Corporate
            (8, "5610591081018250", True),   # Australian BankCard
            (9, "30569309025904", False),    # Diners Club
            (10, "38520000023237", False),   # Diners Club
            (11, "6011111111111117", False), # Discover
            (12, "6011000990139424", False), # Discover
            (13, "6011763916277285", True),  # Discover
            (14, "3530111333300000", True),  # JCB
            (15, "3566002020360505", True),  # JCB
            (16, "5555555555554444", False), # MasterCard
            (17, "5105105105105100", True),  # MasterCard
            (18, "5392799316110230", True),  # MasterCard
            (19, "4111111111111111", False), # Visa
            (20, "4012888888881881", False), # Visa
            (21, "4971023049709545", True),  # Visa
            (22, "4539243436100570", True),  # Visa
            (23, "4556967186646345", True),  # Visa
            (24, "4024007162141435", True),  # Visa
            (25, "4457294243138855", True),  # Visa
            (26, "5357700129102680", True),  # MasterCard
            (27, "5535716632636290", True),  # MasterCard
            (28, "371051674618115", True),   # American Express
            (29, "379924488760905", True),   # American Express
            (30, "343771381317140", True)    # American Express
        ]

        from lab_functions import run_tests_1

        print(run_tests_1(test_data, validate_credit_card))
