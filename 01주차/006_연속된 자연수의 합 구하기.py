N = int(input())

s, e = 1,1
sum, count = 1,1

while e != N:
    if sum > N:
        sum -= s
        s += 1
    elif sum < N:
        e += 1
        sum += e
    else:
        count += 1
        e += 1
        sum += e

print(count)