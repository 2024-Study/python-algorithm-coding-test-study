#다른 방법도 시도해봤으나 결국, 누적합으로 구해야 시간 복잡도를 크게 개선할 수 있음
import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)
    
for i in range(quizNo):
    j, k = map(int, input().split())
    print(prefix_sum[k] - prefix_sum[j-1])
