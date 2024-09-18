#1377

n = int(input())
A = []
max = 0
res = []

for i in range(n):
    A.append(int(input()), i) # (실제 값, 인덱스)

for i in range(n):
    if max < res[i][1] - i:
        max = res[i][1] -i

print(max+1)  # swap 일어나지 않는 반복문이 한 번 더 일어남    
