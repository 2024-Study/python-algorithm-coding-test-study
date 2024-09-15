#12891
'''
o(n)
addDna() 와 deleteDna() 메서드
'''

# n : DNA 문자열 길이, m : 부분 문자열 길이 저장
n,m = map(int, input().split())

# DNA 문자열 배열로 저장
dna = list(input())

# 문자 최소 개수 배열로 저장 A,C,G,T
c = list(map(int, input().split()))
# 부분 문자열의 각 문자 개수 저장 A,C,G,T
p = [0]* 4

# 변수 초기화 s, s+m-1
s = 0  # 부분문자열 시작점
count = 0  

# 추가되는 문자 처리 함수
def addDna(ch):
    if ch == 'A':   
        p[0] += 1
    elif ch =='C':
        p[1] += 1

    elif ch == 'G':
        p[2] += 1
    
    elif ch == 'T': 
        p[3] += 1


# 제거되는 문자 처리 함수
def deleteDna(ch):
    if ch == 'A':   
        p[0] -= 1
    elif ch =='C':
        p[1] -= 1

    elif ch == 'G':
        p[2] -= 1
    
    else: 
        p[3] -= 1


# 조건 확인 함수
def checkDna():
    global count
    if (c[0] <= p[0] and c[1] <= p[1] and c[2] <= p[2] and c[3] <= p[3]):
        count += 1
 
  
  
# 초기 윈도우 설정 ( 길이 m 만큼의 초기 문자열 처리)
for i in range(m):
    addDna(dna[i])

# 초기 윈도우 확인
checkDna()
  
# 슬라이딩 윈도우 시작
for j in range(m ,n):
    addDna(dna[j])
    deleteDna(dna[s])
    s += 1        # 시작점 한 칸 이동
    checkDna()    # 윈도우 확인
    
print(count)

