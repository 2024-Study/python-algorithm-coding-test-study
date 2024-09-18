n = list(input())

for i in range(len(n)):
    max = i
    for j in range(i,len(n)):
        if int(n[j])>int(n[max]):
            max = j
    n[i], n[max] = n[max],n[i]

for i in range(len(n)):
    print(n[i],end='')