# filename: "practice2.py"
import random
'''
Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

def random_element(a):
    ...

fruits = ['apples', 'bananas', 'pears']
random_element(fruits) could return 'apples', 'bananas' or 'pears'
'''
def random_element(a):
    # food_list[random_number]
    # random_number = random.randrange(len(a))
    # return a[random_number]
    return a[random.randrange(len(a))]

# out_string = ''
# for num in range(100):
#     out_string += random_element(['yes', 'no'])
# print(out_string)

def my_repl():
    numbers_list = []
    while True:
        user_input = input("Enter a number or (done): ")
        if user_input.lower() == 'done':
            break
        numbers_list.append(int(user_input))
    return numbers_list
print(my_repl())
