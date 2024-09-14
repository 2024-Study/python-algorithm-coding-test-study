import sys

input = sys.stdin.readline

n = int(input())
origin = []
for i in range(n):
    origin.append((int(input()), i))
sorted = sorted(origin)
num = [0] * n

for i in range(n):
    num[i] = sorted[i][1] - i + 1

print(max(num))
