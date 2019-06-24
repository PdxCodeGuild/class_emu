# lab14_pick6_V2.py
'''
** Version 2 **
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
'''
import random # imports the random module for random number generation
earnings = 0 # defines earnings and starts with a balance of 0 to be incremented by following code
expenses = 0 # defines expenses and starts with a balance of 0 to be incremented by following code
winning_numbers = [] # defines an empty list of winning_numbers to be populated by code below
for i in range(6): # a for loop to set a range of 6 to be appended with random numbers with code below
    winning_numbers.append(random.randint(1,99)) # for 6 itereations from above, appends winning_numbers with 6 random numbers between 1 and 99
for steps in range(100000): # a for loop to set a range of 100,000 iterations of the code below
    expenses -= 2 # subtracts 2 from each iteration of buying a ticket
    user_numbers = [] # defines an empty list of user_numbers to be populated by code below
    for i in range(6): # a for loop to set a range of 6 to be appended with random numbers with code below
        user_numbers.append(random.randint(1,99)) # for 6 itereations from above, appends user_numbers with 6 random numbers between 1 and 99
    matches = 0 # defines variable matches to be incremented by code below
    for j in range(len(user_numbers)): # a for loop to set a range and length of user_numbers to count how many matches there are
        if winning_numbers[j] == user_numbers[j]: # if statement to determine if winning_numbers [j] (index of winning_numbers) matches the same index in user_numbers
            matches += 1 # if the above is true, increments matches by 1
            # print(matches)
    # payouts = [0, 4, 7, 100, 50000, 1000000, 25000000] list can be used instead of below if/elif statements
    # balance += payouts[matches] can be used to determine matches to incrementing payouts instead of if/elif statements below
    if matches == 1: # if statement is true and equals 1 then code below runs
        earnings += 4 # if code runs, increments earnings by 4
    elif matches == 2: # if statement is true and equals 2 then code below runs
        earnings += 7 # if code runs, increments earnings by 7
    elif matches == 3: # if statement is true and equals 3 then code below runs
        earnings += 100 # if code runs, increments earnings by 100
    elif matches == 4: # if statement is true and equals 4 then code below runs
        earnings += 50000 # if code runs, increments earnings by 50000
    elif matches == 5: # if statement is true and equals 5 then code below runs
        earnings += 1000000 # if code runs, increments earnings by 1000000
    elif matches == 6: # if statement is true and equals 6 then code below runs
        earnings += 25000000 # if code runs, increments earnings by 25000000
print(f'Earnings are: ${earnings}') # prints the amount of earnings after all 100000 itereations are run by the above for loop
print(f'Expenses are : ${expenses}') # prints the amount of expenses after all 100000 itereations are run by the above for loop
print(f'ROI is: ${(earnings - expenses)/expenses}') # prints the ROI after all 100000 itereations are run by the above for loop
