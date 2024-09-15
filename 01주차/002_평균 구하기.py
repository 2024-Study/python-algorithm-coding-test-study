# n = int(input())
# scores = list(map(int, input().split()))
# max = max(scores)
# sum = 0

# for i in scores:
#     sum += i / max * 100
    
# print (sum / n)


'''
- 파이썬에는 최댓값 내장함수 존재
- 변수 자료형 조심하기
- input() 은 항상 문자열로 받아오기에 정수형변환 필요
    - 정수형 리스트로 받아오는 방법 : list(map(int, input().split()))
 
- sum 도 내장 함수 존재!

'''

n = int(input())
scores = list(map(int, input().split()))
max = max(scores)
sum = sum(scores)

print(sum * 100 / max / n)
