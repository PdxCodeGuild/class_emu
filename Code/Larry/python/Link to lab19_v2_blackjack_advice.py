# filename: lab19_v2_blackjack_advice.py
'''
Lab 19: Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Version 2 (optional)
Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.

e.g. A = [1, 11], A + A = [2, 12, 22], A + A + A = [3, 13, 33]
'''

from sys import argv # for using sys.argv e.g. $python filename.py run_tests

def play_blackjack(cards):

    # Figure out the point value of each card individually
    # Note: Number cards are worth their number, all face cards are worth 10

    card_value_total = 0
    how_many_aces = 0
    for card in cards:
        if card in ["J", "j", "Q", "q", "K", "k"]:
            card_value = 10
        elif card in ["A", "a"]:
            card_value = 0 # if missing, error:"local variable 'card_value' referenced before assignment"
            how_many_aces += 1
        else:
            card_value = int(card)
        card_value_total += card_value

    # check how the aces (values: 1, 11) will affect the card_value_total

    if how_many_aces == 1:
        if card_value_total + 11 > 21: # if adding 11 makes card_value_total > 21
            card_value_total += 1      # use Ace=1
        else:                          # else implies> if adding 11 makes card_value_total <= 21
            card_value_total += 11     # use Ace=11
    elif how_many_aces == 2:
        if card_value_total + 12 > 21: # if adding 12 (11+1) makes card_value_total > 21
            card_value_total += 2      # use Aces=2
        else:                          # else implies> if adding 12 makes card_value_total <= 21
            card_value_total += 12     # use Ace=12
    elif how_many_aces == 3:
        if card_value_total + 13 > 21: # if adding 13 (11+1+1) makes card_value_total > 21
            card_value_total += 3      # use Aces=3
        else:                          # else implies> if adding 13 makes card_value_total <= 21
            card_value_total += 13     # use Aces=13

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

if len(argv) == 1: # only execute these lines 'run_tests' is passed

    # Ask the user for three playing cards & convert string to integer
    # e.g. (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
    # Note: 'A' can be worth '1' or '11' in this version

    print("\nLet's play Blackjack.\nEnter one of these values: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\n")
    while True:                                 # stay on this input prompt, ...
        first_card = input("What's your first card? ")
        if len(first_card) > 0: #               # ... unless the user submits at least one character
            break
    while True:                                 # stay on this input prompt, ...
        second_card = input("What's your second card? ")
        if len(second_card) > 0: #               # ... unless the user submits at least one character
            break
    while True:                                 # stay on this input prompt, ...
        third_card = input("What's your third card? ")
        if len(third_card) > 0: #               # ... unless the user submits at least one character
            break
    cards = [first_card, second_card, third_card]

    # Print out the current total point value and the advice.

    print(f"\n{play_blackjack(cards)}\n")

###########################################################
### UNIT TESTS ###
###########################################################

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if len(argv) > 1:
    if argv[1] == 'run_tests':  # argv[1] = first argument after the program name, e.g. py filename.py run_tests

        test_data = [
            (1, ['2', '4', '8'], '14 Hit'),            # 14
            (2, ['A', 'A', 'A'], '13 Hit'),            # 13, three As (11+1+1) - lines 40-44
            (3, ['A', 'A', '4'], '16 Hit'),            # 16, two As (11+1) - lines 35-39
            (4, ['K', '3', '5'], '18 Stay'),           # 18
            (5, ['J', 'Q', 'A'], '21 Blackjack!'),     # 21, one A (1) - lines 30-34
            (6, ['A', '8', '2'], '21 Blackjack!'),     # 21, one A (11) - lines 30-34
            (7, ['9', '7', '6'], '22 Already busted!') # 22
        ]

        from lab_functions import unit_tester_1

        print(unit_tester_1(test_data, play_blackjack))
