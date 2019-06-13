print(f"Let's play Rock, Paper, Scissors!\n")
player_choice = input("Go ahead and make a choice: Rock, Paper, or Scissors? ")
player_choice = player_choice.lower()
list_of_choices = ['rock', 'paper', 'scissors']
import random
cpu_choice = random.choice(list_of_choices)
print(cpu_choice)
if player_choice.lower() == 'rock':
    if cpu_choice == 'scissors':
        print(f"The CPU chose {cpu_choice}: You Win!")
    elif cpu_choice == 'paper':
        print(f"The CPU chose {cpu_choice}: You Lose!")
    else:
         print(f"The CPU chose {cpu_choice}: Tie Game!")
elif player_choice.lower() == 'paper':
    if cpu_choice == 'scissors':
        print(f"The CPU chose {cpu_choice}: You Lose!")
    elif cpu_choice == 'paper':
        print(f"The CPU chose {cpu_choice}: Tie Game!")
    else:
         print(f"The CPU chose {cpu_choice}: You Win!")
    print("You chose Paper!")
else:
    if cpu_choice == 'scissors':
        print(f"The CPU chose {cpu_choice}: Tie Game!")
    elif cpu_choice == 'paper':
        print(f"The CPU chose {cpu_choice}: You Lose!")
    else:
         print(f"The CPU chose {cpu_choice}: You Win!")
    