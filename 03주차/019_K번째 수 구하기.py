import sys

input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))


def quick_sort(start, end, k):
    global A
    if start < end:  ###
        pivot = find_pivot(start, end)
        if pivot == k:
            return
        elif k < pivot:
            quick_sort(start, pivot - 1, k)
        else:
            quick_sort(pivot + 1, end, k)

def swap(i,j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def find_pivot(start, end):
    global A
    if end - start == 1:
        if A[start] > A[end]: swap(start, end)
        return end ###

    m = (start + end // 2) ###
    swap(start, m)
    pivot = A[start]
    i = start + 1 ###
    j = end

    while i <= j:
        while A[i] < pivot and i < len(A)-1: ###
            i += 1
        while A[j] > pivot and j>0: ###
            j -= 1
        if i<=j: ###
            swap(i,j)
            i += 1 ###
            j -= 1 ###

    A[start], A[j] = A[j], A[start] ######## start랑 j랑 swap해야함
    return j


quick_sort(0, n - 1, k - 1)
print(A[k - 1])
