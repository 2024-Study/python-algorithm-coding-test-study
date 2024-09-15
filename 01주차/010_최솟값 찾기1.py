import collections

n, l = map(int,input().split())
deque = collections.deque()
num = list(map(int,input().split()))

for i in range(n):
    while deque and deque[-1][0] > num[i]:
        deque.pop()
    deque.append((num[i],i))
    while deque[0][1] <= i-l:
        deque.popleft()
    print(deque[0][0], end=' ')
