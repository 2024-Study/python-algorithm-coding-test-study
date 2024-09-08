import sys
input = sys.stdin.readline

# n,m 입력받기
n, m = map(int, input().split())

# 배열을 0으로 초기화
arr = [[0] *(n+1) for _ in range(n+1)]
prefix_sum = [[0] *(n+1) for _ in range(n+1)]

# 원배열 입력받기  / 1행1열 부터 입력받도록
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