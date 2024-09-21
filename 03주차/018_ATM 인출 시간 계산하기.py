prev = 0
total = 0

n = int(input())
m = list(map(int, input().split()))

sorted_m = sorted(m)

for i in sorted_m:
    prev += i
    total += prev
    
print(total)
