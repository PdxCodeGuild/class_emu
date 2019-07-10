


import random
import time



# generates and returns a list of length n, with random values between 0 and 100
def random_list_generator(n):
    random_list = []
    for num in range(n):
        random_num = random.randint(0,100)
        random_list.append(random_num)
    return random_list

# randomly re-arranges a list
def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums)-1)
        nums[i], nums[j] = nums[j], nums[i]

        # t = nums[i]
        # nums[i] = nums[j]
        # nums[j] = t



# checks if a list is sorted
def is_sorted(nums):
    for i in range(len(nums) - 1):
         if nums[i] > nums[i + 1]:
            return False
    return True


def get_time():
    return int(round(time.time() * 1000))

# continues to generate random arrangements until the list is sorted
def bogosort(nums):
    start_time = get_time()
    counter = 0
    while True:
        shuffle(nums)
        counter += 1
        if is_sorted(nums):
            break

    end_time = get_time()
    time_taken = end_time - start_time
    print(f'total time taken: {time_taken/1000} seconds')
    print(f'time per step:    {time_taken/1000/counter} second')
    print(f'steps:            {counter}')



nums = random_list_generator(10)
print(nums)
num_runs = bogosort(nums)
print(num_runs, nums)
