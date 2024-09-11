# 1253

'''
시도1
분석: n이 2000개 이하이고, 2초 이므로 T는 대략 O(n^2)까지 가능
좋은 수 하나를 찾는데 O(n^2) 가 걸리면 총 n^3이 걸리므로 대략 O(nlogn)을 가져야 함
-> 각 수 마다 앞의 문제와 비슷하게 정렬 & 투포인트 이동 사용 
  *단 자기자신 제외하기
'''

'''
# 수의 개수 n 입력받기
# n개의 수 입력받아 저장
# 정렬
# 변수 초기화
# 모든 수에 대해 좋은 수 인지 확인 (for문)
# s,e 인덱스 양 끝에 두고 합이 해당 수가 되는 쌍이 있으면 count++ 하고 break
'''

# # 수의 개수 n 입력받기
# n = int(input())

# # n개의 수 입력받아 저장
# arr = list(map(int, input().split()))

# # 정렬
# arr.sort()

# # 변수 초기화
# s = 0
# e = 0
# sum = 0
# count = 0
# # 자기 자신보다 작은 모든 수에 대해 좋은 수 인지 확인 (for문)
# # s,e 인덱스 양 끝에 두고 합이 해당 수가 되는 쌍이 있으면 count++ 하고 break


# for i in range(n):
#     s = 0
#     e = i - 1
#     while s < e:
#         if arr[e] == arr[i]:
#             break
#         sum = arr[s] + arr[e]
#         if sum == arr[i]:
#            count += 1
#            break
#         elif sum < arr[i]:
#             s += 1
#         else:
#             e -= 1
            
# print(count)

'''
음수가 존재할 경우를 생각하지 못함 
-3 1 3 5 6 8  인 경우 5 =-3 +8 의 조합으로 좋은 수 임 
'''


# 수의 개수 n 입력받기
n = int(input())

# n개의 수 입력받아 저장
arr = list(map(int, input().split()))

# 정렬
arr.sort()

# 변수 초기화
sum = 0
count = 0

# 자기자신 제외 모든 수에 대해 좋은 수 인지 확인 (for문)
# s,e 인덱스 양 끝에 두고 합이 해당 수가 되는 쌍이 있으면 count++ 하고 break

for i in range(n):
    s = 0
    e = n-1
    while s < e:
        if e == i:
            e -= 1
            # continue
        if s == i:
            s += 1
            # continue
            
        sum = arr[s] + arr[e]
        if sum == arr[i]:
           count += 1
           print(arr[s], arr[e])
           break
        elif sum < arr[i]:
            s += 1
        else:
            e -= 1
            
print(count)