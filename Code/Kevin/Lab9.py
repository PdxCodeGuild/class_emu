nums = [5, 0, 8, 3, 4, 1, 6, 7, 8, 9]
loop_counter = 0
num_sum = 0
for num in nums:
    num_sum += nums[loop_counter]
    loop_counter+=1

print(f"Sum: {num_sum}\nAverage: {num_sum/loop_counter}")

