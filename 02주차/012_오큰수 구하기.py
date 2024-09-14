n = int(input())
A = list(map(int, input().split()))
result = []
for i in range(0, n):
    for j in range(i + 1, n):
        if A[j] > A[i]:
            result.append(A[j])
            break
    else:
        result.append(-1)

for ele in result:
    print(ele, end=" ")
