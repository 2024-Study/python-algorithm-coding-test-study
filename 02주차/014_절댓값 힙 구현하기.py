import sys
from queue import PriorityQueue
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
queue = PriorityQueue()


for i in range(n):
    new = int(input())
    if new == 0:
        if queue.empty():
            print('0\n')
        else:
            temp = queue.get()
            print(str(temp[1])+'\n')
    else:
        queue.put((abs(new), new))