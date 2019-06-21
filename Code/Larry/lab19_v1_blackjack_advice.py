# filename: lab19_v1_blackjack_advice.py
'''
Lab 19: Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

• Less than 17, advise to "Hit"
• Greater than or equal to 17, but less than 21, advise to "Stay"
• Exactly 21, advise "Blackjack!"
• Over 21, advise "Already Busted"

Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit
#
# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay
#
# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!
'''

# # Ask the user for three playing cards & convert string to integer
# # e.g. (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
# # Note: 'A' is worth '1' in this version
# print("Let's play Blackjack. Enter one of these values: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)")
# first_card = int(input("What's your first card? "))
# second_card = int(input("What's your second card? "))
# third_card = int(input("What's your third card?" ))
# cards = [first_card, second_card, third_card]

# Then, figure out the point value of each card individually
# Note: Number cards are worth their number, all face cards are worth 10

def play_blackjack(cards):

    card_value_total = 0
    for card in cards:
        if card in ["J", "j", "Q", "q", "K", "k"]:
            card_value = 10
        elif card in ["A", "a"]:
            card_value = 1
        else:
            card_value = int(card)
        card_value_total += card_value

    # Rules:
    # • Less than 17, advise to "Hit"
    # • Greater than or equal to 17, but less than 21, advise to "Stay"
    # • Exactly 21, advise "Blackjack!"
    # • Over 21, advise "Already Busted"

    if card_value_total < 17:
        return f"{card_value_total} Hit"
    elif 17 <= card_value_total < 21:
        return f"{card_value_total} Stay"
    elif card_value_total == 21:
        return f"{card_value_total} Blackjack!"
    elif card_value_total > 21:
        return f"{card_value_total} Already busted! (sad trombone)"

# Ask the user for three playing cards & convert string to integer
# e.g. (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
# Note: 'A' is worth '1' in this version

print("Let's play Blackjack.\nEnter one of these values: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\n")
first_card = input("What's your first card? ")
second_card = input("What's your second card? ")
third_card = input("What's your third card? ")
cards = [first_card, second_card, third_card]

# Print out the current total point value and the advice.

print(play_blackjack(cards))
