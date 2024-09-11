#10986

'''
내 풀이 : 시간초과
'''
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# prefixSum = [0]
# temp = 0
# res = 0

# # 합 배열 만들어두기
# for i in (arr):
#     temp = temp + i
#     prefixSum.append(temp)
    
# # m으로 나눠 떨어지는 구간 합 개수 구하기
# for i in range (n):
#     for j in range (i+1, n+1):
#         if ((prefixSum[j] - prefixSum[i]) % 3 == 0):
#             res += 1

# print(res)

''' 
합 배열을 먼저 구하고 -> 나머지 배열을 구한다음 -> 나머지 배열의 값이 0인  경우 + 같은 값을 가지는 것 중 2개를 뽑는 경우의 수
'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

# 합 배열과 나머지 배열 초기화
preSum = [0]
temp = 0
remainder = [0] 
r = 0
c = [0]*(m)
res = 0

# 합 배열 구하기 / 인덱스 1부터 시작
for i in arr:
    temp += i
    preSum.append(temp)

# 합 배열의 나머지 배열 구하기
for i in range (1, n+1):
    r = preSum[i] % m
    remainder.append(r)
    c[r] += 1
    
    
# 나머지 배열 값이 0인 경우 + 나머지 배열 값이 같은 경우 중 2개 택(조합)    
for i in range(m):
    if (i == 0):
        res += c[0]
    if (c[i] > 1):
        res += (c[i] * (c[i]-1)) // 2
            
print(res)
print(c)
    
