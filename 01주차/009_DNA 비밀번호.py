check = [0] * 4
current = [0] * 4
checkSecret = 0

def add(c):
    global check, current, checkSecret
    if c == 'A':
        current[0] += 1
        if current[0] == check[0]:
            checkSecret += 1
    elif c == 'C':
        current[1] += 1
        if current[1] == check[1]:
            checkSecret += 1
    elif c == 'G':
        current[2] += 1
        if current[2] == check[2]:
            checkSecret += 1
    elif c == 'T':
        current[3] += 1
        if current[3] == check[3]:
            checkSecret += 1

def remove(c):
    global check, current, checkSecret
    if c == 'A':
        if current[0] == check[0]:
            checkSecret -= 1
        current[0] -= 1
    elif c == 'C':
        if current[1] == check[1]:
            checkSecret -= 1
        current[1] -= 1
    elif c == 'G':
        if current[2] == check[2]:
            checkSecret -= 1
        current[2] -= 1
    elif c == 'T':
        if current[3] == check[3]:
            checkSecret -= 1
        current[3] -= 1

s, p = map(int, input().split())
ans = 0
dna = list(input())
check = list(map(int,input().split()))

for i in range(4):
    if check[i] == 0:
        checkSecret += 1

for i in range(p):  #첫 윈도우
    add(dna[i])

if checkSecret == 4:
    ans += 1

for i in range(p,s):
    j = i - p
    add(dna[i])
    remove(dna[j])
    if checkSecret == 4:
        ans += 1

print(ans)