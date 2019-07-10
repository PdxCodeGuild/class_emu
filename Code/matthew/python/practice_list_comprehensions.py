

#                      2^0 2^1 2^2 2^3
# first 10 powers of 2 [1,  2,  4,  8, 16, 32, 64, 128, 256, 512]
nums = [2**i for i in range(10)]

nums = []
for i in range(10):
    x = 2**i
    nums.append(x)

#                     i  0  1  2  3  4   5   6   7   8   9
# first 10 even numbers [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
nums = [2*i+2 for i in range(10)]
nums = [2*i for i in range(1, 11)]
nums = [i for i in range(2, 21, 2)]
nums = [i for i in range(2, 21) if i % 2 == 0]
# print(nums)



# def min(a, b):
#     return a if a < b else b
# 
#     if a < b:
#         return a
#     else:
#         return b


cc = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'
# cc = '9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9'

# Convert the input string into a list of ints
cc = cc.split(' ')
cc = [int(num) for num in cc]

# Slice off the last digit. That is the check digit.
check_digit = cc.pop(-1)

# Reverse the digits.
cc = [cc[i] for i in range(len(cc)-1, -1, -1)] # cc.reverse()

# Double every other element in the reversed list.
# a if condition else b, evaluates to a if condition is true, else it will evaluate to b
cc = [cc[i]*2 if i % 2 == 0 else cc[i] for i in range(len(cc))]
# for i in range(len(cc)):
#     if i % 2 == 0: # only every other number
#         cc[i] *= 2

# Subtract nine from numbers over nine.
# cc = [cc[i]-9 if cc[i] > 9 else cc[i] for i in range(len(cc))] # iterate over indices
cc = [num-9 if num > 9 else num for num in cc] # iterate over values

total = sum(cc)
if total > 99 or total % 10 != check_digit:
    print('invalid')
else:
    print('valid')

# if sum(cc) % 10 == check_digit:
#     print('valid')
# else:
#     print('invalid')





