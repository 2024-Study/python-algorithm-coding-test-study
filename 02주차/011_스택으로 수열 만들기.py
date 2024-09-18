n = int(input())
stack = []
answer = []
num = 1
result = 0

for i in range(n):
    s = int(input())
    while s >= num:
        stack.append(num)
        answer.append("+")
        num += 1
    if stack[-1] == s:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        result = 1
        break

if result == 0:
    for i in answer:
        print(i)
