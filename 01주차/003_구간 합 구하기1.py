import copy

arr = list(map(int,input().split()))
n = arr[0]
m = arr[1]
a = list(map(int,input().split()))

s = copy.deepcopy(a)

#합 배열 만들기
for i in range(1,n):
    s[i] = s[i-1] + a[i]

sum = []
s.insert(0,0)

for t in range(m):
    arr = list(map(int,input().split()))
    sum.append(s[arr[1]] - s[arr[0]-1])

for i in sum:
    print(i)

##### 답안 #####
# import sys
# input = sys.stdin.readline
# suNo, quizNo = map(int,input().split())
# numbers = list(map(int,input().split()))
# prefix_sum = [0]
# temp = 0    #--> 리스트를 조회할 필요가 없게 해줌
#
# for i in numbers:
#     temp = temp+i
#     prefix_sum.append(temp)
#
# for i in range(quizNo):
#     s,e = map(int,input().split())
#     print(prefix_sum[e] - prefix_sum[s-1])