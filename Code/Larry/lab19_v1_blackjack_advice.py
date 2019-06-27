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
'''
import sys # for using sys.argv e.g. $python3 this_file.py run_tests

def play_blackjack(cards):

    # Figure out the point value of each card individually
    # Note: Number cards are worth their number, all face cards are worth 10

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

    if card_value_total < 17:                       # 3 - 16
        return f"{card_value_total} Hit"
    elif 17 <= card_value_total < 21:               # 17 - 20
        return f"{card_value_total} Stay"
    elif card_value_total == 21:                    # 21
        return f"{card_value_total} Blackjack!"
    elif card_value_total > 21:                     # 22 - 30
        return f"{card_value_total} Already busted!"

if len(sys.argv) == 1: # only execute these lines when 'run_tests' is not passed

    # Ask the user for three playing cards & convert string to integer
    # e.g. (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
    # Note: 'A' is worth '1' in this version

    print("\nLet's play Blackjack.\nEnter one of these values: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\n")
    first_card = input("What's your first card? ")
    second_card = input("What's your second card? ")
    third_card = input("What's your third card? ")
    cards = [first_card, second_card, third_card]

    # Print out the current total point value and the advice.

    print(f"\n{play_blackjack(cards)}\n")

###########################################################
### UNIT TESTS ###
###########################################################

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if len(sys.argv) > 1:
    if sys.argv[1] == 'run_tests':  # 1 first argument after the program name, e.g. py filename.py run_tests

        test_data = [
            (1, ['A', '8', '2'], '11 Hit'),            # 11
            (2, ['2', '4', '8'], '14 Hit'),            # 14
            (3, ['K', '3', '5'], '18 Stay'),           # 18
            (4, ['J', 'Q', 'A'], '21 Blackjack!'),     # 21
            (5, ['9', '7', '6'], '22 Already busted!') # 22
        ]

        from lab_functions import run_tests_1

        print(run_tests_1(test_data, play_blackjack))
