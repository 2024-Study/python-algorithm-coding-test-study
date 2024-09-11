#1940
'''
시도1 : 시간 초과
'''
# # 재료 개수
# n = int(input())

# # 갑옷이 완성되는 번호의 합
# m = int(input())

# # 재료들
# arr = list(map(int, input().split()))

# # 변수 초기화
# startIndex = 0
# endIndex = 1
# count = 0

# # 투 포인트 이동으로 합이 m이 되는 두쌍의 재료 찾기 ( )
# for i in range(n-1):
#     for j in range(i, n):
#         if (arr[i] + arr[j] == m) :
#             count += 1
#             break
            
# print(count)

'''
O(nlogn)인 알고리즘 사용해도 괜춘 -> 정렬 사용
정렬한다음 end와 start 이동시키면서 구하기
'''

# 재료 개수
n = int(input())

# 갑옷이 완성되는 번호의 합
m = int(input())

# 재료들
arr = list(map(int, input().split()))
arr.sort()   # 정렬

# 변수 초기화
s = 0    # 제일 작은 수
e = n-1  # 제일 큰 수
count = 0

# 투 포인트 이동으로 합이 m이 되는 두쌍의 재료 찾기 
# 양 끝에서 sum의 값에 따라 가운데로 이동하는
while s < e :
    sum = arr[s] + arr[e]
    # sum > m : sum - arr[e], s가 오른쪽으로 이동
    if sum > m:
        e -= 1
    # sum < m : sum - 현재 인덱스 s값 + 다음 인덱스 s값, s가 오른쪽으로 이동
    elif sum < m:
        s += 1
    # sum == m : 둘다 가운데로 이동, count +1
    else: 
        s += 1
        e -= 1
        count += 1
        
print(count)