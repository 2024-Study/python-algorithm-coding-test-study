# 2750

n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

    
# 계속 인접한 두 수를 비교해 끝부분부터 완성해나가는 
for i in range(n-1):   
    for j in range(n-1-i):
        if A[j] > A[j+1]: 
            temp = A[j+1]
            A[j+1] = A[j]
            A[j] = temp
        
for i in A:
    print(i)