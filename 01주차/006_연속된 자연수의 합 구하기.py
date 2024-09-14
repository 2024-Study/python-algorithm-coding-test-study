import sys

input = sys.stdin.readline

# 자연수 받아오기
n = int(input())  # n이 10,000,000 -> 시간복잡도 O(n)이어야함.

# 자기 자신일때 미리 카운트
cnt = 1
# 투 포인터 인덱스 초기화
start = 1
end = 1
sum = 1  # 시작 합 1

# 끝 인덱스부터 하나씩 늘려나가며 합을 계산. 합이 n인 경우 카운트 세고 시작 인덱스 이동 (sum 초기화 필요)
while end != n:
    if sum < n:  # 합 만족 X -> 끝 인덱스 이동
        end += 1
        sum += end
    elif sum == n:  # 합 만족 -> 카운트 계산
        cnt += 1
        end += 1
        sum += end
    else:  # 합보다 큼 -> 시작 인덱스 이동
        sum -= start
        start += 1

print(cnt)
