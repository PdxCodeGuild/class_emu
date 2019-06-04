# Lab 10: Average Numbers
# average_numbers_v2.py

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

Version 2

Ask the user to enter the numbers one at a time, putting them into a list.
If the user enters 'done', then calculate and display the average.
The following code demonstrates how to add an element to the end of a list.

nums = []
nums.append(5)
print(nums)
Below is an example input/output:

> enter a number, or 'done': 5
> enter a number, or 'done': 3
> enter a number, or 'done': 4
> enter a number, or 'done': done
average: 4

'''
# Start with the following list
# nums = [5, 0, 8, 3, 4, 1, 6]

# Ask the user to enter the numbers one at a time, putting them into a list.
# If the user enters 'done', then calculate and display the average.

nums = []
while True:
    userinput_num = input("Enter a number, or 'done': ")
    if userinput_num == "done":
        if len(userinput_num) > 0:
            break
    else:
        nums.append(int(userinput_num))

# iIterate through the list
# Keep a 'running sum'
num = 0
for i in range(len(nums)):
    num += nums[i]

# Divide that sum by the number of elements in that list
my_average = num / len(nums)
print(my_average)
