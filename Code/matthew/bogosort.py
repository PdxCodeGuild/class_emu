
import random
import time

def random_list(n):
    counter = 0
    random_number_list = []
    while counter != n:
        counter += 1
        random_number_list.append(random.randint(0, 99))
    return random_number_list


# Larry's algorithm™
def random_list2(n):
    nums = list(range(100))
    random.shuffle(nums)
    return nums[:n]

# Matthew's algorithm™
def random_list3(n):
    nums = []
    while len(nums) < n:
        x = random.randint(0, 99)
        if x not in nums:
            nums.append(x)
    return nums



# def sqrt_both_solutions(x):
#     x **= 0.5
#     return x, -x
# a, b = sqrt_both_solutions(4)
# print(a)
# print(b)


def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums)-1)
        
        # t = nums[i]
        # nums[i] = nums[j]
        # nums[j] = t
        
        nums[i], nums[j] = nums[j], nums[i]
        


def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            return False
    return True


# def bogosort(nums):
#     counter = 0
#     while True:
#         shuffle(nums)
#         counter += 1
#         print(nums)
#         if is_sorted(nums):
#             break
#     print(counter)

def get_time():
    return int(round(time.time() * 1000))

def bogosort(nums):
    count = 0
    start_time = get_time()


    while not is_sorted(nums):
        shuffle(nums)
        count += 1

    end_time = get_time()
    time_taken = end_time - start_time
    print(f'total time taken: {time_taken/1000} seconds')
    print(f'time per step:    {time_taken/1000/count} second')
    print(f'steps:            {count}')




nums = random_list(10) # [56, 67, 21, 4, 78, 98, 12, 13, 65, 32]
print(nums)
bogosort(nums)
print(nums)


# print(nums)
# print(is_sorted(nums))
# nums.sort()
# print(nums)
# print(is_sorted(nums))



# for char in sorted('hello world'):
#     pass
# 
# for element in reversed(['apple', 'banana', 'pear'])
#     pass



