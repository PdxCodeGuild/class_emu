card_values = {'A': 1, '2': 2, '3': 3,'4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'K': 10, 'Q': 10}
first_card = input("What's your first card?:     ")
second_card = input("What's your second card?:     ")
third_card = input("What's your third card?:     ")

player_sum = card_values[first_card] + card_values[second_card] + card_values[third_card]
if player_sum < 17:
    print(f"{player_sum} Hit")
elif player_sum > 17 and player_sum < 21:
    print(f"{player_sum} Stay")
elif player_sum == 21:
    print(f"{player_sum} Blackjack!")
elif player_sum > 21:
    print(f"{player_sum} Already Busted!")