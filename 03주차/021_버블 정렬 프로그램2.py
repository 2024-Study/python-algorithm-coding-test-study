import sys
input = sys.stdin.readline
answer = 0

def merge_sort(s, e):
    global answer
    if s < e:
        m = (s + e) // 2
        merge_sort(s, m)
        merge_sort(m+1, e)

        for i in range(s, e+1):
            tmp[i] = A[i]
        
        k = s
        index1 = s
        index2 = m + 1

        # 병합
        while index1 <= m and index2 <= e:
            if tmp[index1] > tmp[index2]:
                A[k] = tmp[index2]
                answer = answer + index2 - k  # 뒤쪽 값이 앞쪽 값보다 작으면 answer 업데이트
                k += 1
                index2 += 1
            else:
                A[k] = tmp[index1]
                k += 1
                index1 += 1
        # 나머지 데이터 처리
        while index1 <= m:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
        
        while index2 <= e:
            A[k] = tmp[index2]
            k += 1
            index2 += 1

n = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * (n + 1)
merge_sort(1, n)
print(answer)
