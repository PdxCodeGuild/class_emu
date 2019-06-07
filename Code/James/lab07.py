# lab07.py

# imports random module
import random
# assigns a name to the list of possible choices
game_options = ['rock', 'paper', 'scissors']
# assigns a name to the random module that will
comp_pick = random.choice(game_options)

user_pick = input("rock, paper, or scissors?")
# user_pick = user_pick.lower()

# if comp_pick == 'rock' and user_pick == 'rock':


# rock = 'rock'
# if comp_pick == rock:

if comp_pick == 'rock':
    if user_pick == 'rock':
        print("Tie")
if comp_pick == 'paper':
    if user_pick == 'paper':
        print("Tie")
if comp_pick == 'scissors':
    if user_pick == 'scissors':
        print("Tie")
if comp_pick == 'rock':
    if user_pick == 'paper':
        print("You Win")
if comp_pick == 'paper':
    if user_pick == 'rock':
        print("You Lose")
if comp_pick == 'rock':
    if user_pick == 'scissors':
        print("You Lose")
if comp_pick == 'scissors':
    if user_pick == 'rock':
        print("You Win")
if comp_pick == 'scissors':
    if user_pick == 'paper':
        print("You Lose")
if comp_pick == 'paper':
    if user_pick == 'scissors':
        print("You Win")
