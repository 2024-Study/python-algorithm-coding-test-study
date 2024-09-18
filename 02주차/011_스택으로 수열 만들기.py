# 1874

# 입력값 받기
n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
    
    
# 변수 설정
i = 1   # 자연수
j = 0   # 리스트의 인덱스
s = []  # 스택
res = ''   # 결과 
posibility = True

# 구현: 주어진 리스트를 다 읽을 때까지 
# 자연수의 크기와 리스트의 값을 비교
while j < n:
    if i < list[j]:     # 자연수가 리스트의 값보다 작은 경우 : push -> + 추가 -> 자연수++
        s.append(i)
        res += "+\n"
        i += 1
    elif i == list[j]:   # 자연수가 리스트의 값과 같은 경우 : push -> + 추가 -> pop -> - 추가 -> 인덱스++, 자연수++
        s.append(i)
        res += "+\n"
        s.pop()
        res += "-\n"
        i += 1
        j += 1
    else:                # 자연수가 리스트의 값보다 큰 경우 :
        if list[j] == s[-1] :     # 스택 헤드의 값과 리스트의 값과 비교 : 같으면 pop
            s.pop()
            res += "-\n"
            j += 1
        else : 
            posibility = False    # 같지 않으면 불가능한 문제
            break

if posibility:
    print(res)
else:
    print('NO')