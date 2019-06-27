


# x = 10
# 
# def add(a, b):
#     c = a + b
#     return c
# 
# temp = 67
# result = None
# if temp > 60:
#     result = 'warm'
# else:
#     result = 'cold'
# print(result)
# 
# for i in range(100):
#     j = 55
#     pass
# print(i)
# print(j)




# matrix = []
# rows = 4
# cols = 4
# for i in range(rows):
#     matrix.append([])
#     print(matrix)
#     for j in range(cols):
#         v = 1 if i == j else 0
# 
#         # v = None
#         # if i == j:
#         #     x = 1
#         # else:
#         #     v = 0
#         # print(v)
# 
# 
#         matrix[i].append(v)
#         print(matrix)
#     print()
# print(matrix)
# 
# 
# fruits = ['apple', 'banana', 'pear']
# fruits[-1]
# fruits[len(fruits)-1]




# s = 'hello world'
# print(s[0]) #h
# print(s[2:5]) #llo
# print(s[2:5:2]) # lo
# 
# 
# fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocados', 'tomatoes']
# print(fruits[1]) # bananas
# print(fruits[2:5]) # pears, cherries, avocados
# print(fruits[2:5:2]) # pears, avocados

print(list(range(5)))



print('hi', sep=' ', end='\n')
print(5, 6, 7, 8, 9, sep='! ')


# x = 5
# if x in range(0, 100):
#     print('x is in range!')
# 
# if x > 0 and x < 100:
# 
# for i in range(0, 100):
#     if i == x:
#         print('x is in range!')



for i in range(100):
    print(i)

for char in 'hello world!':
    print(char)

#           0          1          2          3          4           5
# fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocados', 'tomatoes']
# 
# fruit = fruits[0]
# fruit = fruit + '!'
# 
# for fruit in fruits:
#     print(fruit)
#     fruit += '!'
# print(fruits)
# 
# for i in range(len(fruits)):
#     print(fruits[i])
#     fruits[i] += '!'
# print(fruits)
# 
# fruit_prices = [['apples', 1.0], ['pears', 2.0]]
# for fruit_price in fruit_prices:
#     fruit_price[1] += 0.5
# print(fruit_prices)




# print(list(range(100,201)))


fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocados', 'tomatoes']

# fruits2 = fruits.copy()
# fruits2[0] = 'pineapple'
# print(fruits)
fruits.insert(3, 'pineapple')
print(fruits)


pineapple = fruits.pop(3)
print(fruits)

index = fruits.index('bananas')
print(index)

fruits.reverse()
print(fruits)
fruits.sort() # lexicographical order
print(fruits)


#             V
nums = [1, 2, 3, 3, 4, 4 ,5]
nums.remove(3)




fruits1 = ['apples', 'bananas']
fruits2 = ['pears', 'cherries']
fruits1.extend(fruits2)
print(fruits1)



print(list(range(5)))
print(list('hello world!')) # ['h', 'e', 'l', ...]

