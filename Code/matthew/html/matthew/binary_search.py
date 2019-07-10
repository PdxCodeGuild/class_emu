

import random



# O(n^2)
def find_duplicates(nums):
    r = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                r.add(nums[i])
    return list(r)


# O(n)
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return None

# O(log(n))
def binary_search_iterative(nums, target):
    lower = 0
    upper = len(nums)-1
    while upper > lower:
        middle = (lower + upper) // 2
        # print(f'{lower} - {upper}')
        # print(f'nums[{middle}] = {nums[middle]}')
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            lower = middle
        else:
            upper = middle

# O(log(n))
def binary_search_recursive(nums, target, lower, upper):
    if lower >= upper:
        return None
    middle = (lower + upper) // 2
    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        lower = middle
    else:
        upper = middle
    return binary_search_recursive(nums, target, lower, upper)


# test code
for i in range(20):
    nums = [random.randint(0,99) for i in range(25)]
    nums = list(set(nums))
    nums.sort()
    target_index = random.randint(0, len(nums)-1)
    target = nums[target_index]

    # print(nums)
    # print(target)
    # print('-'*20)

    # index = linear_search(nums, target)
    # print(f'expected {target_index}, got {index}')
    index = binary_search_iterative(nums, target)
    # print(f'expected {target_index}, got {index}')
    if index != target_index:
        print('error')
