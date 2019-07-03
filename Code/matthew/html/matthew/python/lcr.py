
"""
Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on their turn, rather than rolling all three. When a player has zero chips, he/she passes the dice on their turn, but may receive chips from others and take his next turn accordingly. The winner is the last player with chips left. He/she does not roll the dice, and wins the center pot. If he/she chooses to play another round, he/she does not roll 3, he/she keeps his pot and plays with that."""


import random

# get the names of the players

# players = []
# chips = []

# while True:
#     player_name = input("Enter player name or done when finished:")
#    if player_name.lower() == 'done':
#        break
#    players.append(player_name)
#    chips.append(3)





players = ['matthew', 'lane', 'drew', 'kat', 'darren', 'charlie']
random.shuffle(players)
chips = [3, 3, 3, 3, 3, 3]
die = ['L', 'C', 'R', '.', '.', '.']
pot = 0

def die_number(chips):
    if chips <= 3:
        return chips
    else:
        return 3

def count_chips():
    for index in range(len(chips)):
        if chips[index] + pot == len(chips)*3:
           return players[index]

def print_game():
    for index in range(len(players)):
        print(players[index]+': '+str(chips[index]))


keep_playing = True

while keep_playing:
    for i in range(len(players)):
        # figure out the # of die they'll roll
        die_rolls = die_number(chips[i])
        if die_rolls > 0:
            input(players[i] + ', roll the die! ')
        # roll the dice, move chips
        for j in range(die_rolls):
            die_roll = random.choice(die)
            print(die_roll, end=' ')
            if die_roll == 'L':
                chips[i] -= 1
                chips[i-1] += 1
            elif die_roll == 'C':
                pot += 1
                chips[i] -= 1
            elif die_roll == 'R':
                chips[i] -= 1
                k = i + 1
                if k == len(chips):
                    k = 0
                chips[k] += 1
        print()
        print_game()
        win_check = count_chips()
        if win_check is not None:
            print("The winner is " + win_check)
            keep_playing = False
            break


print(chips, pot)



# give the winning player the pot
