# # n = int(input().split())
# # m = int(input().split())

# n,m = int(input.split())
# num = list(map(int, input()))
# sum = [0]

# for i in num:
#     sum[i+1] = sum[i] + num

# for j in range(m):
#     a,b = input.split()
#     print(sum[b] - sum[a-1])

# n = int(input().split())
# m = int(input().split())


import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
temp = 0

for i in num:
    temp += i
    sum.append(temp)

for j in range(m):
    a,b = map(int, input().split())
    print(sum[b] - sum[a-1])

