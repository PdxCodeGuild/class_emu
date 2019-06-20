x = input("Input a number between 0 and 999:\n")
x = int(x)
hundreds_digit = x // 100
tens_digit = (x//10) % 10
ones_digit = x % 10

hundreds_place = {1: 'One hundred', 2: 'Two hundred', 3: 'Three hundred', 4: 'Four hundred', 5: 'Five hundred', 6: 'Six hundred', 7: 'Seven hundred', 8: 'Eight hundred', 9: 'Nine hundred'}
tens_place = {2: 'Twenty-', 3: 'Thirty-', 4: 'Forty-', 5: 'Fifty-', 6: 'Sixty-', 7: 'Seventy-', 8: 'Eighty-', 9: 'Ninety-'}
ones_place = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens_digits = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', ' Sixteen', 'Seventeen', 'Eighteen', 'Ninteen']

worded_number = ''    

if hundreds_digit == 0 and tens_digit == 0 and ones_digit == 0:
    worded_number = 'zero'
    print(worded_number)
elif hundreds_digit >= 1:
    worded_number += hundreds_place[hundreds_digit]
    #print(hundreds_place[hundreds_digit])


if tens_digit == 0:
    worded_number += ones_place[ones_digit -1]
    print(worded_number)
elif tens_digit == 1:
    worded_number += tens_digits[ones_digit]
    print(worded_number)
else:
    worded_number += tens_place[tens_digit]
    worded_number += ones_place[ones_digit -1]
    print(worded_number)
