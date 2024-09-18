# 1427

A = list(input())
l = len(A)

for i in range(l):
    max = i 
    for j in range(i+1, l):
        if A[j] > A[max]:
            max = j
    if A[i] < A[max]:
        temp = A[i]
        A[i] = A[max]
        A[max] = temp

res = ""
for i in A:
    res += str(i)
    
print(res)