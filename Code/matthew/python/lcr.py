
'''
LCR

Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

If a player has fewer than three chips left, they're still in the game but their number of chips is the number of dice they roll on his/her turn, rather than rolling all three. When a player has zero chips, he/she passes the dice on their turn, but may receive chips from others and take his next turn accordingly. The winner is the last player with chips left. He/she does not roll the dice, and wins the center pot. If he/she chooses to play another round, he/she does not roll 3, he/she keeps his pot and plays with that.
'''
import random




# #           0          1          2
# fruits = ['apples', 'bananas', 'pears']
# # print(fruits[0]) # apples
# # print(fruits[3]) # crash
# # fruits[3] = 'cherries' # crash
# fruits.append('cherries') # adding an element
# fruits[0] += '!' # ['apples!', ...] # updating a value
# 
# 
# fruit_prices = {'apples': 1.0, 'bananas': 1.5, 'pears': 0.8}
# # print(fruit_prices['apples']) # 1.0
# # print(fruit_prices['cherries']) # crash
# fruit_prices['cherries'] = 5.0 # adding a key-value pair
# fruit_prices['cherries'] += 1.0 # updating a value
# 
# fruits = ['apples', 'bananas', 'pears']
# fruits = {0: 'apples', 1: 'bananas', 2:'pears'}
# fruits[0] # apples


# for the dice roll, use random.choice()
def roll_dice(n):
    # return list of n strings that are either: L, C, R, or (dot)
    rolls = []
    for i in range(n):
        die = ["L", "C", "R", ".", ".", "."]
        roll = random.choice(die) #randomly choose one side of a die
        rolls.append(roll)
        # print(roll)
    return rolls

# get left player
def get_left_player(players, current_player_index):
    return players[current_player_index - 1]

# get right player
def get_right_player(players, current_player_index):
    return players[(current_player_index + 1)%len(players)]

# check win
def check_win(players):
    # pass
    counter = 0
    # iterate over players list
    for player in players:
        if player["chips"] >= 1:
            counter += 1
    # print(counter)
    return counter == 1


# assume we know someone won
def find_winner(players):
    
    num_players_with_chips = 0
    for player in players:
        if player["chips"] >= 1:
            num_players_with_chips += 1
    
    # num_players_with_chips = sum([1 if player['chips'] > 0 else 0 for player in players])
    
    if num_players_with_chips == 1:
        for player in players:
            if player["chips"] > 0:
                return player
    return None
    


# players = []
# while True:
#     # input for user names until done
#     name = input("Please enter your name or (done): ")
#     if name == 'done':
#         break
#     players.append({"name": name, "chips": 3})

players = [{
    'name': 'James',
    'chips': 3
},{
    'name': 'Brian',
    'chips': 3
},{
    'name': 'Matt',
    'chips': 3
},{
    'name': 'Larry',
    'chips': 3
},{
    'name': 'Kevin',
    'chips': 3
}]

# # game loop
center_chips = 0
while True:
    for i in range(len(players)):
        player = players[i]
        if player["chips"] != 0:
            # if more than 3 chips, still only 3 rolls
            if player["chips"] > 3:            
                rolls = roll_dice(3)
            else:
                rolls = roll_dice(player["chips"])
            # print(rolls)
            for roll in rolls:
                print(player['name'] + ' rolled a ' + roll + '!')
                if roll == "L":
                    left_player = get_left_player(players, i)
                    left_player["chips"] += 1
                    players[i]["chips"] -= 1
                elif roll == "R":
                    right_player = get_right_player(players, i)
                    right_player["chips"] += 1
                    players[i]["chips"] -= 1
                elif roll == "C":
                    center_chips += 1
                    players[i]["chips"] -= 1
                else:
                    pass
            # print(players)
        winner = find_winner(players)
        if winner is not None:
            winner['chips'] += center_chips
            center_chips = 0
            print(f"{winner['name']} won with {winner['chips']} chips")
            exit()


# print(players)

# print(get_left_player(players,3)) # example
# print(get_right_player(players,3)) # example
# print(roll_dice(4)) # example
# print(check_win(players))





        

        


