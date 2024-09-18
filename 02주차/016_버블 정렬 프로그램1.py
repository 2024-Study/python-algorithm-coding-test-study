import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = []
max = 0
for i in range(n):
    a.append((int(input()),i))

a.sort()

for i in range(n):
    temp = a[i][1] - i
    if temp > max:
        max = temp

print(str(max+1))