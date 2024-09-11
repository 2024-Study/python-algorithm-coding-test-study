#deque를 이용하는 문제
#deque: 양끝에서 삽입, 삭제 가능

from collections import deque #deque 사용
N, L = map(int, input().split()) #N:데이터 개수, L:최솟값을 구하는 범위
mydeque = deque() #데이터를 담을 덱 구조
now = list(map(int, input().split())) #주어진 숫자 데이터를 가지는 리스트

for i in range(N): #N만큼 반복
    while mydeque and mydeque[-1][0] > now[i]: #덱의 마지막 위치에서부터 현재 값보다 큰 값은
        mydeque.pop() #제거
    mydeque.append((now[i], i)) #덱의 마지막 위치에 현재 값 저장
    if mydeque[0][1] <= i - L: #덱의 첫 번째 위치에서부터 L의 범위를 벗어난 값을
        mydeque.popleft() #덱에서 제거
    print(mydeque[0][0], end=' ') #덱의 첫 번째 데이터 출력
