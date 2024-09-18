import sys
import collections
input = sys.stdin.readline

n = int(input())
deq = collections.deque(range(1,n+1))

while len(deq) > 1:
    deq.popleft()
    deq.append(deq[0]) #deq.append(deq.popleft()) 로 줄여쓰기 가능
    deq.popleft()

print(deq[0])