# 001 숫자의 합 구하기
# 11720

n = input()
num = list(input())
res = 0

for i in num:
    res += int(i) # 처음에 list(i)로 써서 틀림 파이썬 문법 주의

print(res)


"""""
파이썬에서 입력값 받는 방법

- 주로 input() 함수 사용 : 입력한 데이터를 문자열로 반환
- 정수로 받으려면 data = int(input())

- 여러 개의 입력 값을 한 줄에 받기 (공백 구분)
    - split() 함수 
    - a, b = input().split()
    - a, b = map(int, input().split())
    
- 리스트 형태로 입력받기
    - num = list(map(int, input().split()))
    
- 여러 줄 입력받기
    - for 루프 사용
    -   n = int(input())  # 몇 줄을 입력받을지 결정
        lines = [input() for _ in range(n)]  # n줄의 입력을 리스트에 저장
        print(lines)

    
 list에 대해 for문 돌리기
    - 1. 기본 for문 사용
    - 2. range()와 len() 사용한 접근
    - 3. enumerate()를 사용한 인덱스와 값 동시 접근
    - 4. 리스트 내포 (List compression)
    - 5. zip()을 사용한 여러 리스트를 동시에 반복
"""