# filename: lab14_v2_pick6.py
'''
Lab 14: Pick6

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the
ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines
the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches.
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net
winnings (the sum of all expenses and earnings).

    • a ticket costs $2
    • if 1 number matches, you win $4
    • if 2 numbers match, you win $7
    • if 3 numbers match, you win $100
    • if 4 numbers match, you win $50,000
    • if 5 numbers match, you win $1,000,000
    • if 6 numbers match, you win $25,000,000

One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for
both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number
of matches between the winning numbers and the ticket.

Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along
with your earnings and expenses.
'''

import random

# Generate a list of 6 random numbers representing the winning tickets
def six_numbers():
    random_6_numbers = []
    for i in range(6):
        random_6_numbers.append(random.randint(0,99))
    return random_6_numbers

# Check which elements & positions match between random_6_numbers (winning) and my_guess (ticket)
def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

random_6_numbers = six_numbers() # set the random_6_numbers (winning numbers)
balance = 0 # Start your balance at $0
payout_dict = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000} # dictionary of matches:payout
earnings = 0 # Start your earnings at $0
for i in range(100000): # Loop 100,000 times
    my_guess = six_numbers() # Generate a list of 6 random numbers representing the ticket
    balance -= 2 # Subtract $2 from your balance (you bought a ticket)
    matches = num_matches(random_6_numbers, my_guess) # call num_matches(), parameters=random numbers lists
    balance += payout_dict[matches] # add winnings to the balance
    earnings += payout_dict[matches] # track (add to) the earnings (amount won)

# After the loop, print the final balance
# format snippet: https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string
print(f"Balance: ${format (balance, ',d')}")

# Calculate your ROI, print it out along with your earnings and expenses.
# The ROI (return on investment) = (earnings - expenses)/expenses
# earnings = dollar amount of payouts; expenses = $2 * 100,000 guesses = $200,000
print(f"ROI: {(earnings - 200000)/200000}")
