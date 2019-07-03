
import random
# problem 6 ================================================

def count_letter(find_letter, word):
    counter = 0
    for letter in word:
        if letter == find_letter:
            counter += 1
    return counter

for i in range(10):
    word = 'antidisestablishmentarianism'
    letter = random.choice(word)
    print(letter, count_letter(letter, word)) # 5

#print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2


print(random.choice(list({'name': 'jose', 'age': 'whatever'}.keys())))
