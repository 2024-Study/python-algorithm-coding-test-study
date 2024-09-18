import sys
input = sys.stdin.readline

k = 1
num = []
stack = []
result = []

n = int(input())
for _ in range(n):
    a = int(input())
    while a >= k:
        stack.append(k)
        result.append('+')
        k += 1
    if a < k:
        temp = stack.pop()
        if temp != a:
            result = ['NO']
            break
        else:
            result.append('-')
            num.append(temp)

for i in result:
    print(i)