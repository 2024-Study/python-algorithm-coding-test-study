import sys
input = sys.stdin.readline

n,m = map(int,input().split())
temp,ans = 0, 0
s = []
c = [0]*m

a = [int(x) for x in input().split()]

#합 배열
for i in a:
    temp += i
    s.append(temp)

for i in range(n):
    temp = s[i] % m
    if temp == 0:
        ans+=1
    c[temp] += 1

for i in c:
    ans += i * (i-1) // 2

print(ans)