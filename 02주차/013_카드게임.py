#2164

from collections import deque
n = int(input())

queue = deque()

for i in range (1, n+1):
    queue.append(i)

for i in range (1, n):
    queue.popleft()
    queue.append(queue.popleft())
    
    
# n-1번 끝나면 1장 남음 마지막 한 장 출력
print(queue[0])