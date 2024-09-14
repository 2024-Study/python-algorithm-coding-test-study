from heapq import heappush, heappop
import sys

input = sys.stdin.readline

heap = []

count = int(input())
for _ in range(count):
    n = int(input())

    if not n:
        print(heappop(heap)[1] if heap else 0)
        continue

    heappush(heap, (abs(n), n))
