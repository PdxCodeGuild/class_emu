# lab20_credit_card_validation.py
'''
Lab 20: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''
# Ask user for input then convert the input string into a list of ints
input_cc = input("What is the credit card number to check? Enter numbers with spaces. Example: 4 5 5 6 7 3: ")
cc = input_cc.split(' ')
cc = [int(num) for num in cc]
# print(cc)
# Slice off the last digit. That is the check digit.
check_digit = cc.pop(-1)
# print(check_digit)
# Reverse the digits.
cc.reverse()
# print(cc)
# Double every other element in the reversed list.
cc = [cc[i]*2 if i % 2 == 0 else cc[i] for i in range(len(cc))]
# print(cc)
# Subtract nine from numbers over nine.
cc = [num-9 if num > 9 else num for num in cc]
# print(cc)
# Sum all values.
total = sum(cc)
# print(total)
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
if total > 99 or total % 10 != check_digit:
    print('Invalid')
else:
    print('Valid')
