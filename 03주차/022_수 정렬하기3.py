import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
count = [0] * 10001

for i in range(n):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(f"{i}\n")


# 기수 정렬로 구현했더니 메모리 초과...
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# from queue import Queue
#
# n = int(input())
# A = [int(input()) for _ in range(n)]
# queue_list = []
# for _ in range(10):
#     queue_list.append(Queue())
#
# for i in range(5):
#     for j in range(n):
#         num = A[j] % pow(10,i+1) // pow(10,i)
#         queue_list[num].put(A[j])
#     A.clear()
#     for j in range(10):
#         while not queue_list[j].empty():
#           A.append(queue_list[j].get())
#
# for i in range(n):
#     print(f"{A[i]}\n")