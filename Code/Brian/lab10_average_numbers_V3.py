# L10_average_numbers_V3.py
'''
** Version 3 **

Calculate the median. The median is the number in the middle when the list is sorted.
If there's an even number of numbers, the median is a list of the two numbers in the middle.
Remember the sort method on lists.
'''

num_list = [5, 0, 8, 3, 4, 1, 6] # defines varialbe nums into a list of numbers
num_list.sort() # sorts the list from lowest to highest number (or a to z if words)
median = len(num_list) // 2 # calculates the median (of odd numbered list) by taking the length of the sorted list and doing floor division by 2
print(median) # prints the median
