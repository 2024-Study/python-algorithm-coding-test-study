n = int(input())
score = input().split()
m, sum, k = 0, 0, 0

#최댓값 찾기
for i in score:
    if int(i) > m:
        m = int(i)

#점수 변환
for i in score:
    score[k] = int(i)/m*100
    k+=1

#변환한 점수 합 구하기
for i in score:
    sum += i

#평균 출력
print(sum/len(score))


##### 답안 #####
# n = int(input())
# list = list(map(int,input().split()))
# max = max(list)
# sum = sum(list)
# print(sum*100/max/n) #수식을 변환하여 로직을 간단히 하기
