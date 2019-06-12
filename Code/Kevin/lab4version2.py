print("Welcome, USERNAME, to the Magic 8-Ball program!\n")
user_Input = input("Go ahead, ask the Magic 8-Ball a question. PS. Make it challenging!\n")
magic_Answers = ['Probably', 'Most Definitely', 'I don\'t see it in the cards']
import random
print(random.choice(magic_Answers))
while True:
    user_Input = input("Have another question? Enter done to quit\n")
    user_Input = user_Input.lower()
    if user_Input == 'done':
        break
    print(random.choice(magic_Answers))
