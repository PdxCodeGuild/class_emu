 # lab19_blackjack_advice_V1.py
'''
Lab 19: Blackjack Advice

** Version 1 **

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
Then, figure out the point value of each card individually.
Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.
Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

What's your first card? Q       What's your first card? K       What's your first card? Q
What's your second card? 2      What's your second card? 5      What's your second card? J
What's your third card? 3       What's your third card? 5       What's your third card? A
15 Hit                          20 Stay                         21 Blackjack!
'''

print("Please tell me your 3 cards and then I will give you blackjack advice, so you can become RICH!! ") # prints statement
user_card1 = input("Enter your first card: ").upper() # defines variable and prompts user for input
user_card2 = input("Enter your second card: ").upper() # defines variable and prompts user for input
user_card3 = input("Enter your third card: ").upper() # defines variable and prompts user for input
if user_card1 not in 'A2345678910JQK' or user_card2 not in 'A2345678910JQK' or user_card3 not in 'A2345678910JQK': # if statement is true, below code will run
    print("Sorry, that is not valid for blackjack. ") # prints statement if above is True
    quit() # quits the program
print(f"Your cards are: {user_card1}, {user_card2} and {user_card3}") # if the above is false, prints.  f' is so inside {} will run as code

def card_value(card): # defines a function called card_value with parameter card
    if card == 'A': # if statement to determine if the card is an A, below code runs
        return 1 # if above is True, returns a value of 1 for the card
    elif card == 'J' or card == 'Q' or card == 'K': # if statement to determine if the card is an J, Q or K... below code runs
        return 10 # if above is True, returns a value of 10 for the card
    return int(card) # if both statements above are False, returns the integer value of the card

total = card_value(user_card1) + card_value(user_card2) + card_value(user_card3) # gets card value total by adding all card values
print(f"You have a total of {total} ") # prints the statement.  f' allows data inside {} to run as code

if total < 17: # if True, below code runs
    print('You should Hit')
elif total < 21: # if True, below code runs
    print('You should Stay')
elif total == 21: # if True, below code runs
    print('Blackjack! You win!')
else: # if all above are False, below code runs
    print('Already Busted')
