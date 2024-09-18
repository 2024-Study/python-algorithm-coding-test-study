'''
틀린 문제
틀린 이유 : 정렬 전 인덱스 - 정렬 후 인덱스 아이디어를 떠올리지 못함
또한, swap이 일어나지 않는 반복문이 한 번 더 실행되는 것을 감안해 최댓값+1을 해야 하는 점을 떠올리지 못함
'''
import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i)) #정렬 기준을 고려하여 데이터, index 순서로 저장
    
max = 0
sorted_a = sorted(a)

for i in range(n):
    if max < sorted_a[i][1] - i: #[정렬 전 index - 정렬 후 index] 계산의 최댓값 저장
        max = sorted_a[i][1] - i
        
print(max + 1)
