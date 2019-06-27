



def count_cats(animals):
    counter = 0
    for animal in animals:
        if animal == 'cat':
            counter += 1
    return counter

# print(count_cats(['cat', 'cat', 'dog', 'mouse', 'cat'])) # 3


def is_even(a):
    return a % 2 == 0

def eveneven(nums):
    counter = 0
    for num in nums:
        if is_even(num):
            counter += 1
    return is_even(counter)

# print(eveneven([5, 6, 2])) # true
# print(eveneven([5, 5, 2])) # false




def print_every_other(nums):
    for i in range(0, len(nums), 2):
        print(nums[i])
    
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 2


# nums = [2, 12, 22, 32, 42, 52, 62, 72, 82]
# print_every_other(nums) # 2, 22, 42, 62, 82


def reverse(fruits):
    fruits = fruits.copy()
    fruits.reverse()
    return fruits
    
    # r = []
    # for fruit in fruits:
    #     # r.insert(len(r), fruit)
    #     r.insert(0, fruit)
    #     print(r)
    # return r
    
    # r = []
    # for i in range(len(fruits)-1, -1, -1):
    #     r.append(fruits[i])
    # return r
    
    # fruits = fruits.copy()
    # for i in range(len(fruits)//2):
    #     j = len(fruits)-i-1
    # 
    #     # fruits[i] = fruits[j]
    #     # fruits[j] = fruits[i]
    # 
    #     t = fruits[i]
    #     fruits[i] = fruits[j]
    #     fruits[j] = t
    # 
    # return fruits
    
    
    

# fruits = ['apples', 'bananas', 'cherries']
# print(reverse(fruits)) # cherries, bananas, apples
# print(fruits)




def extract_less_than_ten(nums):
    # create a temporary list
    temp_list = []
    # iterate, check if item is less than 10
    for num in nums:
        if num < 10:
            # if so, add it to the temporary list
            temp_list.append(num)
    
    # return the temporary list
    return temp_list

# nums = [2, 4, 6, 8, 10, 12, 14, 16]
# print(nums)
# print(extract_less_than_ten(nums)) # 2, 4, 6, 8



def common_elements(nums1, nums2):
    common = []
    
    # loop over the first list
    # for each element, check if the element is in the second list
    # if it is, add it to the output list
    
    for num in nums1:
        if num in nums2:
            common.append(num)
    
    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                common.append(num1)
    
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                common.append(nums1[i])
    
    # for i in range(len(nums1)):
    #     for j in range(len(nums2)):
    #         print(i, j)
    # 
    # if nums1[0] == nums2[0]:
    #     common.append(nums1[0])
    # if nums1[0] == nums2[1]:
    #     common.append(nums1[0])
    # if nums1[0] == nums2[2]:
    #     common.append(nums1[0])
    # if nums1[0] == nums2[3]:
    #     common.append(nums1[0])
    # 
    # if nums1[1] == nums2[0]:
    #     common.append(nums1[1])
    # if nums1[1] == nums2[1]:
    #     common.append(nums1[1])
    # if nums1[1] == nums2[2]:
    #     common.append(nums1[1])
    # if nums1[1] == nums2[3]:
    #     common.append(nums1[1])
    # 
    # if nums1[2] == nums2[0]:
    #     common.append(nums1[2])
    # if nums1[2] == nums2[1]:
    #     common.append(nums1[2])
    # if nums1[2] == nums2[2]:
    #     common.append(nums1[2])
    # if nums1[2] == nums2[3]:
    #     common.append(nums1[2])
    
    return common
    


# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6])) # [3, 4]



def combine(list1, list2):
    combined = []
    
    # combined.append(list1[0])
    # combined.append(list2[0])
    # combined.append(list1[1])
    # combined.append(list2[1])
    # combined.append(list1[2])
    # combined.append(list2[2])
    
    for i in range(len(list1)):
        combined.append(list1[i])
        combined.append(list2[i])    
    return combined

# print(combine(['a','b','c'], [1,2,3])) # ['a', 1, 'b', 2, 'c', 3]



def find_pair(nums, target):
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return None
    # 
    # if nums[0] + nums[1] == target:
    #     return [nums[0], nums[1]]
    # if nums[0] + nums[2] == target:
    #     return [nums[0], nums[2]]
    # if nums[0] + nums[3] == target:
    #     return [nums[0], nums[3]]
    # 
    # if nums[1] + nums[2] == target:
    #     return [nums[1], nums[2]]
    # if nums[1] + nums[3] == target:
    #     return [nums[1], nums[3]]
    # 
    # if nums[2] + nums[3] == target:
    #     return [nums[2], nums[3]]
    


# print(find_pair([5, 6, 2, 3], 7)) # [5, 2]


def find_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append([nums[i], nums[j]])
    return pairs

# print(find_pairs([5, 6, 2, 3, 1], 7)) # [[5, 2],[6, 1]]



def merge(nums1, nums2):
    output = []
    
    for i in range(len(nums1)):
        temp_list = [] # [nums1[i], nums2[i]]
        temp_list.append(nums1[i])
        temp_list.append(nums2[i])
        output.append(temp_list)
    
    return output

# print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]







# f(n) = f(n-1) + f(n-2)
# n    0  1  2  3  4  5   6   7   8
# f(n) 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibonacci_list(n):
    fib_numbers = [1, 1]
    for num in range(n-1):
        a = fib_numbers[-1]
        b = fib_numbers[-2]
        fib_numbers.append(a + b)
    return fib_numbers

# print(fibonacci_list(7)) # [1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci_v1(n):
    fib_numbers = [1, 1]
    for num in range(n-1):
        a = fib_numbers[-1]
        b = fib_numbers[-2]
        fib_numbers.append(a + b)
    return fib_numbers[-1]

# print(fibonacci_v1(7)) # 21



# a = 1
# b = 1
# loop!
#     c = a + b
#     a = b
#     b = c

def fibonacci_v2(n):
    a = 1
    b = 1
    for num in range(n-1):
        c = a + b
        a = b
        b = c
    return c

# print(fibonacci_v2(7)) # 21


# fib(7)
# fib(6) + fib(5)
# (fib(5) + fib(4)) + fib(5)
# ((fib(4) + fib(3)) + fib(4)) + fib(5)
# (((fib(3) + fib(2)) + fib(3)) + fib(4)) + fib(5)
# ((((fib(2) + fib(1)) + fib(2)) + fib(3)) + fib(4)) + fib(5)
# (((((fib(1) + fib(0)) + fib(1)) + fib(2)) + fib(3)) + fib(4)) + fib(5)

def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# print(fibonacci_recursive(7)) # 21

# 5! = 5*4*3*2*1
# 10! = 10*9*8*7*...
def factorial_v1(n):
    nums = list(range(1, n+1))
    r = 1
    for i in range(len(nums)):
        r *= nums[i]
    return r
    
def factorial_v2(n):
    r = 1
    for k in range(2, n+1):
        r *= k
    return r

# print(factorial_v2(2)) # 120


def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

# print(factorial_recursive(5))

# fac(5)
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120


def minimum(nums):
    # nums = nums.copy()
    # nums.sort()
    # return nums[0]
    
    # return sorted(nums)[0]
    
    rm = nums[0]
    for num in nums:
        if num < rm:
            rm = num
    return rm
    
    
# rm = 88
# if 45 < rm: rm = 45
# if 13 < rm: rm = 13
# if 60 < rm: rm = 60
# if 21 < rm: rm = 21

nums = [88, 45, 13, 60, 21, 5]
print(nums)
print(minimum(nums)) # 13
print(nums)





s = """hello world!"""


s = """
some stuff blah
blah blah blah
"""

s = 'some stuf blah\nblah blah blah'




