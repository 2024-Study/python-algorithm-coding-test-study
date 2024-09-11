#2018

# n 입력받기
n = int(input())

# 변수 초기화 
count = 1       #15=15인 경우
startIndex = 1
endIndex = 1
sum = 1

# start_index와 end_index 이동시키며 count해가기
while endIndex != n:
    # sum이 n보다 작은 경우 : end 포인트 오른쪽으로 이동, sum에 end값 더하기
    if sum < n:
        endIndex += 1
        sum += endIndex
    # sum이 n 보다 큰 경우 : sum에 start 값 빼기, start 포인트 오른쪽으로 이동
    elif sum > n:
        sum -= startIndex
        startIndex +=1
    # sum = n인 경우 : count++, end,start 모두 오른쪽 이동, sum에서 이전 start값 뺴고 현재 end값 더하기
    else: 
        count +=1
        endIndex +=1
        startIndex +=1
        sum = sum - (startIndex-1) + endIndex 

print(count)