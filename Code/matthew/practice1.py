
# def is_even(a):
#     if a % 2 == 0:
#         return True
#     elif a % 2 == 1:
#         return False
#
# def is_even(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
# def is_even(a):
#     if a % 2 == 0:
#         return True
#     return False

def is_even(a):
    return a % 2 == 0

# print(is_even(5))
# print(is_even(6))

def opposite(a, b):
    if a < 0 and b > 0:
        return True
    elif a > 0 and b < 0:
        return True
    else:
        return False

# print(opposite(0, 1))
# print(opposite(-1, 4))
# print(opposite(-1, -2))


# def abs(x):
#     return -x if x < 0 else x

def near_100(num):
    return abs(100 - num) <= 10
    # return num >= 90 and num <= 110

# print(near_100(95))
# print(near_100(105))
# print(near_100(50))
# print(near_100(-95))


def maximum_of_three(a, b, c):

    return a if a > b and a > c else b if b > a and b > c else c

    # nums = [a, b, c]
    # nums.sort()
    # return nums[-1]
    # return nums[2]
    # return nums[len(nums)-1]

    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    return c

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

# print(maximum_of_three(5, 6, 2))
# print(maximum_of_three(-4, 3, 10))

def power_2():
    for i in range(21):
        print(2 ** i)
power_2()
