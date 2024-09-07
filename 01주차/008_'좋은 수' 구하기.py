n = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for i in range(n):
    find = A[i]  
    left = 0
    right = n - 1
    
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        current_sum = A[left] + A[right]
        if current_sum == find:
            count += 1
            break
        elif current_sum < find:
            left += 1
        else:
            right -= 1
            
print(count)
