# lab14_pick6_V1.py
'''
Lab 14: Pick6
** Version 1 **
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'.
Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff.
Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches.
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match.
Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets.
Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance
'''
import random # imports the random module for random number generation
balance = 0 # defines balance and starts with a balance of 0 to be incremented by following code
winning_numbers = [] # defines an empty list of winning_numbers to be populated by code below
for i in range(6): # a for loop to set a range of 6 to be appended with random numbers with code below
    winning_numbers.append(random.randint(1,99)) # for 6 itereations from above, appends winning_numbers with 6 random numbers between 1 and 99
for steps in range(100000): # a for loop to set a range of 100,000 iterations of the code below
    balance -= 2 # subtracts 2 from each iteration of buying a ticket
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
        balance += 4 # if code runs, increments balance by 4
    elif matches == 2: # if statement is true and equals 2 then code below runs
        balance += 7 # if code runs, increments balance by 7
    elif matches == 3: # if statement is true and equals 3 then code below runs
        balance += 100 # if code runs, increments balance by 100
    elif matches == 4: # if statement is true and equals 4 then code below runs
        balance += 50000 # if code runs, increments balance by 50000
    elif matches == 5: # if statement is true and equals 5 then code below runs
        balance += 1000000 # if code runs, increments balance by 1000000
    elif matches == 6: # if statement is true and equals 6 then code below runs
        balance += 25000000 # if code runs, increments balance by 25000000
print(balance) # prints the balance after all 100000 itereations are run by the above for loop
