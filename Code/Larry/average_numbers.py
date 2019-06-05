# Lab 10: Average Numbers
# average_numbers.py

'''
We're going to average a list of numbers.
1. Start with the following list,
2. iterate through it,
3. keeping a 'running sum',
4. then divide that sum by the number of elements in that list.

Hint: Remember len will give you the length of a list.

Example/Tip:
nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

'''
# Start with the following list
nums = [5, 0, 8, 3, 4, 1, 6]

# iIterate through the list
# Keep a 'running sum'
num = 0
for i in range(len(nums)):
    num += nums[i]

# Divide that sum by the number of elements in that list
my_average1 = num // len(nums)
my_average2 = (num % len(nums)) / len(nums)
print(my_average1 + my_average2)
