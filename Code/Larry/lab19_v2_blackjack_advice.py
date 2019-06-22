# filename: lab19_v2_blackjack_advice.py
'''
Lab 19: Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Version 2 (optional)
Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.

e.g. A = [1, 11], A + A = [2, 12, 22], A + A + A = [3, 13, 33]
'''

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
        if card_value_total + 11 < 21:  # if adding 11 to total equals less than 21
            card_value_total += 11      # use Ace=11
        else:                           # else implies> if adding 11 to total equals greater than 21
            card_value_total += 1       # use Ace=1
    elif how_many_aces == 2:
        if card_value_total + 12 < 21: # if adding 12 (11+1) to total equals less than 21
            card_value_total += 12      # use Ace=1 and Ace=11 or Aces=12
        else:                           # else implies> if adding 12 to total equals greater than 21
            card_value_total += 2       # use Ace=1 and Ace=1 or Aces=2
    elif how_many_aces == 3:
        if card_value_total + 13 < 21:  # if adding 13 (11+1+1) to total equals less than 21
            card_value_total += 13      # use Aces=13
        else:                           # else implies> if adding 13 to total equals greater than 21
            card_value_total += 3       # use Aces=3

    # Rules:
    # • Less than 17, advise to "Hit"
    # • Greater than or equal to 17, but less than 21, advise to "Stay"
    # • Exactly 21, advise "Blackjack!"
    # • Over 21, advise "Already Busted"

    if card_value_total < 17:
        return f"\n{card_value_total} Hit\n"
    elif 17 <= card_value_total < 21:
        return f"\n{card_value_total} Stay\n"
    elif card_value_total == 21:
        return f"\n{card_value_total} Blackjack!\n"
    elif card_value_total > 21:
        return f"\n{card_value_total} Already busted! (sad trombone)\n"

# ''' Uncomment this line to run the tests
# Ask the user for three playing cards & convert string to integer
# e.g. (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
# Note: 'A' is worth '1' in this version

print("Let's play Blackjack.\nEnter one of these values: (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\n")
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
print(play_blackjack(cards))
# '''

###########################################################
### UNIT TESTS ###
###########################################################

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if __name__ == '__main__':

    test_data = [
        ('2', '4', '8', 'Hit'),             # 14
        ('A', 'A', 'A', 'Hit'),             # 13, three As - lines 40-44
        ('A', 'A', '4', 'Hit'),             # 16, two As - lines 35-39
        ('K', '3', '5', 'Stay'),            # 18
        ('J', 'Q', 'A', 'Blackjack!'),      # 21, one A - lines 30-34
        ('9', '7', '6', 'Already busted!')  # 22
    ]

    def run_tests(input_output, function_name):
        failed_test_count = 0
        failed_test_msg = ''
        for i in range(1):
            function_output = function_name(input_output[i][0])
            expected_output = input_output[i][1]
            if function_output != expected_output:
                failed_test_count += 1
                failed_test_msg += f"\n{input_output[i][0]}: Fail.\nExpected Result: {expected_output} ==> Actual result: {function_output}\n"
        if failed_test_count != 0:
                return failed_test_msg
        if failed_test_count == 0:
                return "All tests passed."

        # print(run_tests(test_data, play_blackjack)) # *** uncomment this line to run the unit tests ***
