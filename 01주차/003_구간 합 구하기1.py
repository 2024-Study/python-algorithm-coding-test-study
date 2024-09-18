# # n = int(input().split())
# # m = int(input().split())

# n,m = int(input.split())
# num = list(map(int, input()))
# sum = [0]

# for i in num:
#     sum[i+1] = sum[i] + num

# for j in range(m):
#     a,b = input.split()
#     print(sum[b] - sum[a-1])

# n = int(input().split())
# m = int(input().split())


import sys
input = sys.stdin.readline   # 성능개선을 위함

n,m = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
temp = 0

for i in num:
    temp += i
    sum.append(temp)   # 합배열 만들어두고 

for j in range(m):
    a,b = map(int, input().split())
    print(sum[b] - sum[a-1])   # 만들어둔 합배열로 구간 합 구하기


'''
import sys
input = sys.stdin.readline
# 입력 속도를 높이기 위해 자주 사용됨
# 많은 양의 데이터를 빠르게 입력받아야 하는 경우 유용
# 한 줄을 통째로 문자열오 입력받음 (마지막 줄바꿈 문자도 포함됨 주의 .strip() 사용하면 제거가능)

'''
