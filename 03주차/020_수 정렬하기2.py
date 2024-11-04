import sys
input = sys.stdin.readline
print =sys.stdout.write

n = int(input())
A = [int(input()) for i in range(n)]

def merge_sort(start, end):
    if end - start >= 1:
        mid = (start + end)//2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        merge(start, mid, end)

def merge(start, mid, end):
    global A
    i = start
    j = mid + 1
    temp = []
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    if i<= mid: temp.extend(A[i:mid+1])
    if j <= end: temp.extend(A[j:end+1])
    A[start:end+1] = temp

merge_sort(0, n-1)
for i in range(n):
    print(A[i])