n = int(input())
arr = list(input()) #list() 의 인자로 문자열을 전달하면, 문자 단위로 나누어 list 에 저장
ans = 0

for i in range(n):
    ans += int(arr[i])

print(ans)

##### 답안 #####
# for i in arr:
#     ans += int(i)
