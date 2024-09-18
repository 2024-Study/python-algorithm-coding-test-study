#11286

from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
myQueue = PriorityQueue()
res = ""

for i in range(n):
    req = int(input())
    # 출력
    if req == 0:
        if myQueue.empty():
            res += "0\n"
        else:
            temp = myQueue.get()
            res += str(temp[1]) +"\n"   # 진짜 값인 두번째 튜플이 출력되도록
           
    # 입력
    else:
        # 절댓값 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성 
        # -1 인 경우 : (1, -1)
        # 1 인 경우 : (1, 1)
        myQueue.put((abs(req), req))
        
print(res)