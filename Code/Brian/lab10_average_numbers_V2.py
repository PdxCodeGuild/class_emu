# L10_average_numbers_V2.py

# Version 2
# Ask the user to enter the numbers one at a time, putting them into a list.
#If the user enters 'done', then calculate and display the average.
#The following code demonstrates how to add an element to the end of a list.
# nums = []
# nums.append(5)
# print(nums)
# Below is an example input/output:
#
# > enter a number, or 'done': 5
# > enter a number, or 'done': 3
# > enter a number, or 'done': 4
# > enter a number, or 'done': done
# average: 4

num_list = [] # defines the variable num_list as a blank list
while True: # checks if the value is true and, if so, runs the while loop
    user_input = input("Please type a number, or press 'done' > ") # prompts the user for input
    if user_input == 'done': # will continue to run the loop until the user types "done"
        break # breaks out of the loop if user types "done"
    num_list.append(int(user_input)) # appends the list with user's numbers as integers until user types "done"
print(num_list) # prints the list once outside the loop

def Average(num_list): # defines a function called Average
    return sum(num_list) / len(num_list) # returns the average of the list by dividing the sum by the length
average = Average(num_list) # defines variable average and states it is equal to the function Avereage
print("Average of the list = ", round(average, 2)) # prints the statement and rounds it to the number of digits (2) up to which the given number is to be rounded.
