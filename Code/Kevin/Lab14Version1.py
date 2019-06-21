import random

player_balance = 0
def pick_6():
    nums = []
    for i in range(6):
        nums.append(random.randint(0,99))
        #nums.append(i) #Hard code numbers 0-6
    return nums
def num_matching(winning, ticket):
    matches = []
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches.append(winning[i])
    return matches


winning_ticket = pick_6()

for i in range(100):
    player_ticket = pick_6()
    matching_numbers = num_matching(winning_ticket, player_ticket)
    player_balance -= 2
    if len(matching_numbers) == 1:
        player_balance += 4
    elif len(matching_numbers) == 2:
        player_balance += 7
    elif len(matching_numbers) == 3:
        player_balance += 100
    elif len(matching_numbers) == 4:
        player_balance += 50000
    elif len(matching_numbers) == 5:
        player_balance += 1000000
    elif len(matching_numbers) == 6:
        player_balance += 25000000

    # print(f"Winning Ticket: {winning_ticket}")
    # print(f"Player Ticket: {player_ticket}")
    print(f"Matching Numbers: {matching_numbers}")
    # print(f"Player Balance: {player_balance}")

print(player_balance)