n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
print(*arr, sep="\n")
