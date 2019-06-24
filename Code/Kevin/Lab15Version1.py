x = input("Input a number between 0 and 99:\n")
x = int(x)
tens_digit = x//10
ones_digit = x%10
tens_place = {2: 'Twenty-', 3: 'Thirty-', 4: 'Forty-', 5: 'Fifty-', 6: 'Sixty-', 7: 'Seventy-', 8: 'Eighty-', 9: 'Ninety-'}
ones_place = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teen_digits = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', ' Sixteen', 'Seventeen', 'Eighteen', 'Ninteen']

worded_number = ''    

if tens_digit == 0 and ones_digit == 0:
    worded_number = 'zero'
    print(worded_number)
elif tens_digit == 0:
    worded_number = ones_place[ones_digit -1]
    print(worded_number)
elif tens_digit == 1:
    worded_number = teen_digits[ones_digit]
    print(worded_number)
else:
    worded_number += tens_place[tens_digit]
    worded_number += ones_place[ones_digit -1]
    print(worded_number)
