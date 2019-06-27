
nums = []
while True:
    num = input('enter number: ')
    if num == 'done':
        break
    nums.append(int(num))
print(nums)


exit()


text = 'hello world!'
text2 = ''
for char in text:
    print(text2)
    text2 += char + char
print(text2)
exit()











#            0         1          2         3           4           5
fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocados', 'tomatoes']
# print(len(fruits))
# print(fruits[0])
# print(fruits[-1])
# print(fruits[len(fruits)-1])
# print(fruits[::3])

first_element = fruits.pop(0)
print(first_element)
print(fruits)


fruits2 = fruits.copy()
fruits2.append('pineapple')
print(fruits)
print(fruits2)


# print takes *args
print('hello')
print('hello', 'world')
print('hello', 'goodbye', 'world')



def less_than_five(x):
    if x < 5:
        return 'x is less than five'
        print('this won\'t ever print')
    else:
        return 'x is not less than five'





def sum_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total

nums = [1, 2, 3, 4, 5]
print(sum_numbers(nums))
print(sum_numbers(1, 2, 3, 4, 5))
exit()




def add(a, b):
    return a + b

c = 5
d = 2

print(add(c, d))
c = add(5, 2)

# x is None because say_hello doesn't return anything
def say_hello():
    print('hello!')
x = say_hello()
print(x)
