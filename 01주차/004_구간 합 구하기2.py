'''
많이 헤맨 문제 
!다시 풀어보기!
'''
# 성능향상 위한
import sys
input = sys.stdin.readline

# n,m 입력받기
n, m = map(int, input().split())

# 배열을 0으로 초기화
arr = [[0] *(n+1) for _ in range(n+1)]
prefix_sum = [[0] *(n+1) for _ in range(n+1)]

# 원배열 입력받기  / 1행 1열 부터 입력받도록
for i in range (1, n+1):
    arrRow = list(map(int, input().split()))
    for j in range (1, n+1):
        arr[i][j] = arrRow[j-1] 

# 배열 합 구하기
for i in range (1, n+1):
    for j in range (1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i][j]  # 중요!

# 이차원 구간 합 구하기
for i in range (m):
    a, b, c, d = map(int, input().split())
    print(prefix_sum[c][d] - prefix_sum[a-1][d] - prefix_sum[c][b-1] + prefix_sum[a-1][b-1])
    
    
'''
배열은 0부터 저장되는데 우리는 주로 1부터 생각하기 때문에 이 불일치가 너무 헷갈린다.
원배열을 저장하는 뭔가 더 좋은 아이디어가 있을 것 같다. 

'''