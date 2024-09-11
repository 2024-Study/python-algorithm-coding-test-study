n = int(input())

count = 0
i = 1

while i*(i-1)//2 < n:
    if (n - (i*(i-1)) // 2) % i == 0:
        count += 1
    i += 1
    
print(count)
