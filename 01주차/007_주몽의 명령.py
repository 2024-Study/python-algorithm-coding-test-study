import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num = list(map(int,input().split()))
ans = 0
i, j = 0, n-1

num.sort()

while i < j:
    if num[i]+num[j] > m:
        j -= 1
    elif num[i]+num[j] < m:
        i += 1
    else:
        ans += 1
        i += 1
        j -= 1

print(ans)