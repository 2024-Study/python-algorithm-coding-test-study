import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
stack = []
ans = [-1] * n

for i in range(n):
    new = a[i]
    while len(stack)>0 and new > a[stack[-1]]:
        index = stack.pop()
        ans[index] = new
    stack.append(i)

for i in ans:
    print(i, end=' ')