# filename: lab10_v3_average_numbers.py
'''
Lab 10: Average Numbers

Version 3

Calculate the median.
The median is the number in the middle when the list is sorted.
If there's an even number of numbers, the median is a list of the two numbers in the middle.
Remember the sort method on lists.
'''

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

nums.sort()
print(nums)

if len(nums) % 2 == 1:
    # num is an odd number
    output_odd = nums[len(nums) // 2]
    print(f"The median is {output_odd}.")
if len(nums) % 2 == 0:
    # num is an even number
    output_even1 = nums[len(nums) // 2 - 1]
    output_even2 = nums[len(nums) // 2]
    print(f"The median is {output_even1} & {output_even2}.")
