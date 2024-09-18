#17298

'''
시도1 : 시간 초과
'''
'''
# 입력값 받기
n = int(input())
A = list(map(int, input().split()))

# 변수 설정
stack = []    #스택
NGE = [0]*n    # 오큰수 

# 수열 크기 만큼 반복
for i in range (n):
    
    # 스택이 비어있지 않고 그 다음수가 현재 값보다 큰 경우 : 오큰수 저장 
    while stack and A[i] > A[stack[-1]]:
        NGE[stack.pop()] = A[i]
        
    # 스택이 비어있는 경우 || 그 다음수가 현재 값보다 작은 경우 : push
    stack.append(i)
    
# 다 돌고난 뒤 스택에 남은 것에 대해 오큰수 -1로 설정
while stack:
    NGE[stack.pop()] = -1
    
# 주어진 형식에 맞추어 오큰수 출력
res = ""
for i in NGE:
    res += str(i) + " "
print(res)    
       
'''      
     
     
'''
시도2 : sys 이용, 오큰수 초기값 -1로 설정
'''       
'''
# 입력값 받기
import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# 변수 설정
stack = []    # 스택
NGE = [-1]*n    # 오큰수 (-1로 초기화)

# 수열 크기 만큼 반복
for i in range (n):
    
    # 스택이 비어있지 않고 그 다음수가 현재 값보다 큰 경우 : 오큰수 저장 
    while stack and A[i] > A[stack[-1]]:
        NGE[stack.pop()] = A[i]
        
    # 스택이 비어있는 경우 || 그 다음수가 현재 값보다 작은 경우 : push
    stack.append(i)
    
# 주어진 형식에 맞추어 오큰수 출력
res = ""
for i in NGE:
    res += str(i) + " "
print(res)    

'''
     
        
'''
시도3 : * 언패킹 연산자 사용
cf) * 언패킹 연산자란?
: 리스트나 튜플을 풀어서 개별 요소로 처리하도록 해주는 역할
print(*NGE)는 print 함수에 NGE 리스트의 각 요소를 하나씩 풀어서 전달하는 것
예를 들어, NGE가 [1, 2, 3]이라면, print(*NGE)는 print(1, 2, 3)과 동일하게 작동해서 결과적으로 1 2 3을 출력
'''       

# 입력값 받기
import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# 변수 설정
stack = []    #스택
NGE = [-1]*n    # 오큰수 

# 수열 크기 만큼 반복
for i in range (n):
    
    # 스택이 비어있지 않고 그 다음수가 현재 값보다 큰 경우 : 오큰수 저장 
    while stack and A[i] > A[stack[-1]]:
        NGE[stack.pop()] = A[i]
        
    # 스택이 비어있는 경우 || 그 다음수가 현재 값보다 작은 경우 : push
    stack.append(i)

# 주어진 형식에 맞추어 오큰수 출력

# 이 방법으로는 시간 초과되므로 * 언패킹연산자를 사용하도록 하자
# res = ""
# for i in NGE:
#     res += str(i) + " "
# print(res)    

print(*NGE)
               