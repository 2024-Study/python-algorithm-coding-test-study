n = int(input())
a = list(map(int,input().split()))
result = [-1] * n
stack = []
for i in range(n):
    while stack and a[i]>a[stack[-1]]:
        result[stack[-1]]=a[i]
        stack.pop()
    stack.append(i)
print(*result)
