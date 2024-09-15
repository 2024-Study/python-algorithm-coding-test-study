import sys
input = sys.stdin.readline

size, num = map(int,input().split())
a = []
#s = [[0]*(size+1)]*(size+1)
s = [[0]*(size+1) for _ in range(size+1)]

for i in range(size):
    a.append(list(map(int,input().split())))

#합 배열
for i in range(1,size+1):
    for j in range(1,size+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i-1][j-1]

#질의
for _ in range(num):
    x1,y1,x2,y2 = map(int,input().split())
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])


##### 답안 #####
# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
#
# A=[[0]*(n+1)] #첫번째 행 0으로 초기화
# D=[[0]*(n+1) for _ in range(n+1)] #0으로 모두 초기화
#
# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()] #첫번째 열만 0이 되도록
#     A.append(A_row)
# .
# .
# .