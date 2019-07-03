
import random

# problem 1 ============================================

def random_element(a):
    index = random.randint(0, len(a)-1)
    return a[index]
#
# for i in range(100):
#     fruits = ['apples', 'bananas', 'pears', 'blackberries']
#     print(random_element(fruits))


# problem 2 ============================================

def get_numbers():
    r = []
    while True:
        value = input('Enter a number (or \'done\'): ')
        if value == 'done':
            break
        value = int(value)
        r.append(value)
    return r
#
# print(get_numbers())


# problem 3 ================================================

def is_even(a):
    return a%2 == 0

def eveneven(nums):
    even_counter = 0
    for element in nums:
        if is_even(element):
            even_counter += 1
    return is_even(even_counter)
#
# print(eveneven([5, 6, 2]))
# print(eveneven([5, 5, 2]))

# problem 4 =================================================


def print_every_other_while(nums):
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 2

def print_every_other_for(nums):
    for i in range(0, len(nums), 2):
        print(nums[i])

    for i in range(len(nums)):
        if i%2 == 0:
            print(nums[i])

    for num in nums[::2]:
        print(num)

    for i in range(len(nums))[::2]:
        print(nums[i])

# print_every_other_while([1, 2, 3, 4, 5, 6, 7, 8])
# print_every_other_for([1, 2, 3, 4, 5, 6, 7, 8])



# problem 5 =================================================


# import math
# def sqrt(a):
#     return math.sqrt(a), -math.sqrt(a)
#
# root1, root2 = sqrt(4)


def reverse(nums):

    # nums.reverse()
    # return nums

    # nums = nums[::-1]
    # return nums

    # r = []
    # for num in nums:
    #     # print(num)
    #     r.insert(0, num)
    #     # print(r)
    # return r

    for i in range(len(nums)//2):
        j = len(nums)-i-1
        nums[i], nums[j] = nums[j], nums[i]

        # t = nums[i]
        # nums[i] = nums[j]
        # nums[j] = t
    return nums
#
# print(reverse(list(range(0, 10))))




# def edit_param(a):
#     a.append(4)
#
# a = [1, 2, 3]
# edit_param(a)
# print(a)




# problem 7 ==============================================================

def common_elements(nums1, nums2):
    common = []
    for num in nums1:
        if num in nums2 and num not in common:
            common.append(num)
        # for num2 in nums2:
        #     if num == num2:
        #         common.append(num)
    return common


# print(common_elements([1, 2, 3], [2, 3, 4]))



# problem 8 ==============================================================


def combine(nums1, nums2):
    r = []
    for i in range(len(nums1)):
        r.append(nums1[i])
        r.append(nums2[i])
    return r

# print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]


# problem 9 ==============================================================


def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            #print(f'{i} {j}')
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return None

# print(find_pair([5, 6, 2, 3], 7)) #  [5, 2]



# problem 10 ==============================================================

# this_is_snake_case
# thisIsCamelCase
# ThisIsPascalCase

def merge(nums1, nums2):
    r = []
    for i in range(len(nums1)):
        a = nums1[i]
        b = nums2[i]
        merged = [a, b]
        r.append(merged)
    return r


# print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]



# problem 11 ==========================================================


# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums1.extend(nums2)
# print(nums1) # [1, 2, 3, 4, 5, 6]

# def combine3(list1, list2, list3):
#     return list1 + list2 + list3

# people = [{'name': 'matthew'}, {'name': 'darren'}]
# for i in range(len(people)):
#     print(people[i]['name'])


def combine_all(lists):
    r = []
    for i in range(len(lists)):
        r.extend(lists[i])
        # for j in range(len(lists[i])):
        #     r.append(lists[i][j])
    return r
# print(combine_all([[5,2,3],[4,5,1],[7,6,3]])) # [5,2,3,4,5,1,7,6,3]


# problem 12 ================================================================

#  n   =  0, 1, 2, 3, 4, 5,  6,  7,  8,  9
# f(n) =  1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    fib = [1, 1]
    # fib[i] = fib[i-1] + fib[i-2]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[len(fib)-1]

# print(fibonacci(2))


def minimum(nums):
    if len(nums) == 0:
        return None
    running_min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < running_min:
            running_min = nums[i]
    return running_min

def maximum(nums):
    running_max = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > running_max:
            running_max = nums[i]
    return running_max

def mean(nums):
    running_total = 0
    for num in nums:
        running_total += num
    return running_total / len(nums)


# nums = []
# for i in range(10):
#     nums.append(random.randint(0, 100))
# nums.sort()
# print(nums)
# print(f'min: {minimum(nums)}')
# print(f'max: {maximum(nums)}')
# print(f'mean: {mean(nums)}')


# problem 13 ==================================================================

def find_unique(nums):
    r = []
    for i in range(len(nums)):
        if nums[i] not in r:
            r.append(nums[i])
        # found = False
        # for j in range(len(r)):
        #     if nums[i] == r[j]:
        #         found = True
        #         break
        # if not found:
        #     r.append(nums[i])
    return r
nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(find_unique(nums)) # [12, 24, 35, 88, 120, 155]
