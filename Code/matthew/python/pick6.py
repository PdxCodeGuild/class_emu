
import random




def pick6():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 99))
    return nums


def num_matches(winning, ticket):
    matches = 0
    for j in range(len(ticket)):
        if winning[j] == ticket[j]:
            matches += 1
    return matches


# Generate a list of 6 random numbers representing the winning tickets

winning = pick6()


# Start your balance at 0
balance = 0

# Loop 100,000 times, for each loop:

for i in range(100000):    
    # Generate a list of 6 random numbers representing the ticket
    ticket = pick6()
    
    # Subtract 2 from your balance (you bought a ticket)
    balance -= 2
        
    # Find how many numbers match
    matches = num_matches(winning, ticket)
    
    # Add to your balance the winnings from your matches
    #          0  1  2   3     4       5         6
    payouts = [0, 4, 7, 100, 50000, 1000000, 25000000]
    balance += payouts[matches]
    
    # if matches == 1:
    #     balance += 4
    # elif matches == 2:
    #     balance += 7
    # elif matches == 3:
    #     balance += 100
    # elif matches == 4:
    #     balance += 50000
    # elif matches == 5:
    #     balance += 1000000
    # elif matches == 6:
    #     balance += 25000000
    
# After the loop, print the final balance
print(balance)






