import sys

input = sys.stdin.readline

n = int(input())  # 수의 개수 (2,000)
arr = list(map(int, input().split()))
arr.sort()

# 다른 두 수의 합으로 표현되는 수가 있다면 좋은 수라고 함!
cnt = 0
for target in range(2, n):  # target idx는 2부터 시작(0,1이 시작 인덱스)
    start = 0
    end = target - 1
    while start < end:
        sum = arr[start] + arr[end]
        if sum == arr[target]:  # 현재 합이 같으면 -> 좋은 수로 판단하고 다른 타겟!
            cnt += 1
            break
        elif sum > arr[target]:  # 현재 합이 크면 -> 큰 값 - 1
            end -= 1
        else:  # 현재 합이 작으면 -> 작은 값 +1
            start += 1

print(cnt)
