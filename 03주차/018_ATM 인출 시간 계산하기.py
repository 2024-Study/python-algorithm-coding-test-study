import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int,input().split()))
sum = 0

# for i in range(1,n):
#     for j in range(i):
#         if t[i] < t[j]:
#             t[j],t[i] = t[i],t[j]

for i in range(1,n):
    insert_point = i
    insert_value = t[i]
    # 현재 범위에서 삽입 위치 탐색
    for j in range(i):
        if t[i] > t[j]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    # 삽입을 위해 삽입 위치에서 current index(i)까지 데이터를 한 칸씩 뒤로 밀기
    for j in range(i,insert_point,-1):
        t[j] = t[j-1]
    # 삽입 위치에 current index 데이터 값 저장
    t[insert_point] = insert_value


for i in range(n):
    sum += t[i]*(n-i)

print(sum)

