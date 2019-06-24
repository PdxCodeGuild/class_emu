nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_every_other(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            print(nums[i])


print_every_other(nums)