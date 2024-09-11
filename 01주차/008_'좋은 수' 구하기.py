import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
ans = 0

num.sort()

for m in range(n):
    s, e = 0, n-1
    while s<e:
        if num[s] + num[e] > num[m]:
            e -= 1
        elif num[s] + num[e] < num[m]:
            s += 1
        else:
            if s != m and e != m:
                ans += 1
                break
            elif s == m:
                s += 1
            else:
                e -= 1

print(ans)