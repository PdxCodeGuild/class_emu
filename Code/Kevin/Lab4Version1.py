import random


print("Welcome, USERNAME, to the Magic 8-Ball program!\n")
user_Input = input("Go ahead, ask the Magic 8-Ball a question. PS. Make it challenging!\n")
magic_Answers = ['Probably', 'Most Definitely', 'I don\'t see it in the cards']
print(random.choice(magic_Answers))
