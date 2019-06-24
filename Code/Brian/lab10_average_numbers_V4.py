# L10_average_numbers_V4.py
'''
** Version 4 (optional) **

The mode is the number that occurs the most. There may be multiple modes. Hint: use a dictionary to count the occurances of each number, the key can be the number, the value can be the number of occurances. If it's not in the dictionary, add it and set it's value to one. If it's already in the dictionary, increment that value.

counts = list(word_dict.items()) # .items() returns a list of tuples
counts.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
print(counts)
'''

number_list = [5, 0, 8, 3, 4, 1, 6, 5, 5, 1, 5, 1, 3] # defines variable number_list as list of numbers
number_dict = {} # defines number_dict as an empty dictionary
# for number in number_list: # for loop to determine each number in the number_list
#     number_dict[number] = 0 # sets a dictionary key for each number with a value of 0
# the above 2 lines 14 and 15 are not needed as the below for loop already determines the new numbers starting at 0
for number in number_list: # for loop to determine each number in the number_list
    if number in number_dict: # sets parameter that if a number from the number_list is in the number_dict
        number_dict[number] += 1 # if the about statement is true it will add + 1 to the number
    else: # if the above if statement is false
        number_dict[number] = 1 #it will add the number in the dictionary and give it a value of 1
print(number_dict) # prints the dictionary
