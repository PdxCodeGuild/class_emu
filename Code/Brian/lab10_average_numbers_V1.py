# L10_average_numbers_V1.py

# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
#
# The code below hows how to loop through an array, and prints the elements one at a time.
#
# nums = [5, 0, 8, 3, 4, 1, 6]
#
# # loop over the elements
# for num in nums:
#     print(num)
#
# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])


nums = [5, 0, 8, 3, 4, 1, 6] # defines varialbe nums into a list of numbers
for num in nums: # loops over the list
    print(num) # prints each index with each iteration of the loop
for i in range(len(nums)): # loops over the lenght of the list
    print(nums[i]) # prints each index with each iteration of the loop

def Average(nums): # defines a funtion called Average
    return sum(nums) / len(nums) # returns the average of the list by dividing the sum by the length
average = Average(nums) # defines variable average and states it is equal to the function Avereage
print("Average of the list = ", round(average, 2)) # prints the statement and rounds it to the number of digits (2) up to which the given number is to be rounded.
