# 11003
'''
2.4초 5,000,000 이므로 O(n)으로 해결해야함 -> 정렬 사용X
덱과 슬라이딩 윈도우를 이용해 정렬 효과를 보는 것
덱은 각 요소를 한 번만 처리하므로 매우 효율적
'''

from collections import deque

n,l = map(int, input().split())
arr = list(map (int, input().split()))

mydeque = deque()


# 덱의 마지막 위치에서부터 현재 값보다 큰 값의 덱 제거
# 덱의 마지막 위치에 현재값 저장
# 덱의 1번째 위치에서부터 l 의 범위 벗어난 값 제거
# 덱의 첫번째 데이터 출력
for i in range(n):
    # 현재 값보다 큰 값 가진 요소 제거
    while mydeque and mydeque[-1][0] > arr[i]: # 덱이 비어있지 않고 덱의 마지막 요소가 현재 값보다  큰 경우 
        mydeque.pop()
    
    # 현재값과 인덱스 추가
    mydeque.append((arr[i], i))
    
    # 윈도우 범위를 벗어난 요소 추가
    if mydeque[0][1] <= i - l:
        mydeque.popleft()
        
    
    # 현재 윈도우의 최솟값 출력
    print(mydeque[0][0], end=' ')


'''
파이썬에서 덱

: collections 모듈에서 제공하는 양방향 큐
: 양쪽 끝에서 삽입, 삭제가 가능 
: 양 끝에서 삼입, 삭제 연산에서 O(1)의 빠른 시간 복잡도를 가진다. 

1. 모듈 임포트 : from collections import deque
2. 덱 생성 : d= deque()
3. 요소 추가 : d.append(5), d.appendleft(0)
4. 요소 제거 : d.pop(), d.popleft()
5. 첫번째 요소 접근 : first = d[0]
6. 마지막 요소 접근 : last = d[-1]
7. 덱 길이 확인 : length = len(d)

'''