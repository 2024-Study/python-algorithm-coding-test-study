n = int(input())
nums = [0] * n

for i in range(n):
    nums[i] = int(input())
sorted_nums = sorted(nums)

for i in range(len(nums)):
    print(sorted_nums[i])
