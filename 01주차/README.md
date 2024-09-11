# 📖 학습 요약

## 🔥 학습 내용

| **문제** | **링크**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 필수     | [숫자의 합](https://www.acmicpc.net/problem/11720) / [평균](https://www.acmicpc.net/problem/1546) / [구간 합 구하기1](https://www.acmicpc.net/problem/11659) / [구간 합 구하기2](https://www.acmicpc.net/problem/11660) / [나머지 합 구하기](https://www.acmicpc.net/problem/10986) / [연속된 자연수 합](https://www.acmicpc.net/problem/2018) / [주몽](https://www.acmicpc.net/problem/1940) / ['좋은 수' 구하기](https://www.acmicpc.net/problem/1253) / [DNA 비밀번호](https://www.acmicpc.net/problem/12891) / [최솟값 찾기](https://www.acmicpc.net/problem/11003) |
| 추가     | []()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## ✏️ 개념 정리

# ✨ MEMO

## 0. 코딩 테스트 준비하기

### 시간 복잡도

- 연산 횟수 : 1초에 2,000만 번 연산하는 것을 기준으로 한다.
- 시간 복잡도는 항상 최악일 때, 즉 데이터의 크기가 가장 클 때를 기준으로 한다.

→ 각 알고리즘의 시간복잡도를 계산하여, 입력 크기를 바탕으로 최선의 알고리즘을 채택해야 한다.

### 디버깅

- **F5** : 디버그 시작/정지
- **Shift + F5** : 디버그 종료
- **Ctrl + F5** : 시작(디버그 실행 x)
- **F9** : breakpoint on/off
- **F10** : 디버그 현재 라인 실행(한줄씩 실행), 함수를 만나면 함수 안으로 들어가지 않음
- **F11** : 디버그 함수의 경우 **함수 내부**로 들어가서 실행
- **Shift + F11** : 디버그 하고 있는 현재 함수 빠져나오기

[2-5. VS CODE 사용법 (디버깅)](https://wikidocs.net/137962)

# 1. 자료구조

## 배열과 리스트

파이썬에서는 배열과 리스트의 장점만 가지고 와서 사용이 매우 편하다. (삽입과 삭제가 쉽고, 가변적임)

- **[문제] [숫자의 합](https://www.acmicpc.net/problem/11720)**
  ```java
  n = int(input())
  num = input()
  print(sum(list(map(int, num))))
  ```
  책에서는 입력 자체를 문자 리스트로 받아와 for문을 통해 하나씩 int로 바꿔서 사용..
  나의 경우, num자체를 문자열로 받아오고, 받아온 문자열도 리스트이기때문에, 각 자릿수를 Int로 map하여 합을 구해서 풀이했다.
  → `map` 객체는 이터레이터이므로 리스트로 변환하지 않아도 바로 `sum` 함수에서 처리 가능합니다. 이는 메모리 사용량을 줄이고 성능을 약간 더 최적화하는 방법입니다.
  `print(sum(map(int, num)))` 이렇게 풀이해도 된다는 것!!
- [[문제] 평균 구하기](https://www.acmicpc.net/problem/1546)
  ```java
  n = int(input())
  score = list(map(int, input().split()))
  max_score = max(score)

  # 각 점수 순회하면서 최댓값을 바탕으로 점수 구하기
  for i in range(len(score)):
      score[i] = (score[i] / max_score) * 100

  print(sum(score) / len(score))
  ```
  평균은 모든 값에 같은 식으로 적용되기 때문에, 일일히 점수를 수정하지 않고 합과 최고값을 바탕으로 평균 점수를 쉽게 구할 수 있다.
  ```java
  n = int(input())
  score = list(map(int, input().split()))
  max_score = max(score)
  print(sum(score)/max_score*100/n)
  ```

### ⭐️구간 합

구간합은 합 배열을 이용하여 시간복잡도를 더 줄이기 위해 사용하는 특수한 목적의 알고리즘이다. (사용 빈도가 높음)

합 배열은 주로 S로 표현한다. S[4]는 A[0]~A[4]까지의 합이라고 생각할 수 있다.

- [[문제] 구간 합 구하기 1](https://www.acmicpc.net/problem/11659)
  ```java
  import sys
  input = sys.stdin.readline

  n, m = map(int, input().split())
  arr = list(map(int, input().split()))

  # Prefix Sum 배열 생성
  prefix_sum = [0] * n
  prefix_sum[0] = arr[0]

  # 구간 합 구하기
  for i in range(1, n):
      prefix_sum[i] = prefix_sum[i - 1] + arr[i]

  # 테스트 케이스 진행
  for _ in range(m):
      a, b = map(int, input().split())
      if a == 1:
          print(prefix_sum[b - 1])
      else:
          print(prefix_sum[b - 1] - prefix_sum[a - 2])

  ```
  가장 헷갈렸던 점은 입력의 a, b 값이 인덱스가 아니라 순서를 지정하도록 되어있어서 -1을 추가로 해줘야 했다. 해당 부분은 입력 값을 인덱스로 따로 맞춰주거나, 디버깅을 조금 더 연습하면 좋을 것 같다.
  추가로, 파이썬으로 진행 시 시간초과가 발생하는 문제가 있다. 다음과 같은 방법으로 최적화해주자.
  ```java
  import sys
  input=sys.stdin.readline
  ```
  기본적으로 `input()` 함수는 Python에서 느리기 때문에 많은 양의 입력을 받을 때는 `sys.stdin.readline`을 사용하는 것이 더 효율적이다.
  - `sys.stdin.readline`의 장점
    - **속도**: `sys.stdin.readline`은 버퍼 단위로 입력을 처리하므로 많은 양의 데이터를 빠르게 읽을 수 있다.
    - **줄바꿈 처리**: `sys.stdin.readline`은 입력 뒤에 자동으로 줄바꿈(`\n`)이 포함되므로, 이를 제거하기 위해 추가로 `strip()`을 사용하는 것이 일반적이다.
  ![→ 최적화 결과, 시간이 10배는 더 빨라졌다… 입력 초반에 최적화해주기 잊지 말자!](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dc951d7-030e-4915-afbe-55616c07abf7/4a275635-15e2-4036-9b1b-7b91af948536/image.png)
  → 최적화 결과, 시간이 10배는 더 빨라졌다… 입력 초반에 최적화해주기 잊지 말자!
- [[문제] 구간 합 구하기 2](https://www.acmicpc.net/problem/11660)
  ```java
  import sys
  input = sys.stdin.readline

  n, m = map(int, input().split())

  arr = []
  # 표 작성
  for i in range(n):
      arr.append(list(map(int, input().split())))

  dp = [[0] * (n + 1) for _ in range(n + 1)]  # (n+1)*(n+1) 표 초기화
  # dp 초기화 (구간합 계산)
  for i in range(1, n + 1):
      for j in range(1, n + 1):
          dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
          # 위, 옆의 합 가져와서 구간합 계산

  # 테스트 케이스 실행
  for t in range(m):
      x1, y1, x2, y2 = map(int, input().split())
      result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
      print(result)
  ```
  문제를 풀이할 때 풀이를 메모하고 그려보는 연습이 필요하다고 생각한 부분.
  우선, DP(부분합) 개념을 이용하여 문제를 풀기 위해 빈 배열을 선언해주는 부분 잊지 말자. (다른 방식으로 하면 선언이 제대로 안됨!)
  ```java
  dp = [[0] * (n + 1) for _ in range(n + 1)]  # (n+1)*(n+1) 표 초기화
  ```
  선언 후, 문제의 그림을 바탕으로 구간합을 구하는 점화식을 차근차근 계산한다. 이때 주의해야 할 부분은 arr은 n개의 값이 채워진 반면, dp는 초기화 값 0을 포함하여 n+1개의 값이 있다는 점. 예외 케이스를 고려하며 코드를 짤 수 있다.
  ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dc951d7-030e-4915-afbe-55616c07abf7/dcbf8fd3-14fb-4e04-bedb-d8931233f12e/image.png)
- [[문제] 나머지 합 구하기](https://www.acmicpc.net/problem/10986)
    <aside>
    📌
    
    **첫번째 풀이 : 슬라이딩 윈도우 (시간초과 발생)**
    
    </aside>
    
    ```java
    import sys
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 구간 합 구하기
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = arr[i] + dp[i]
    
    # 연속된 구간의 길이를 하나씩 늘려가며, 나누어떨어지는 개수를 카운트하자
    cnt = 0
    for t in range(1, n + 1):  # term이 1부터 n까지 늘어남 3
        for j in range(1, n - t + 2):  # 체크할 구간 시작점 2
            sub_sum = dp[j + t - 1] - dp[j - 1]
            if sub_sum % m == 0:
                cnt += 1
    
    print(cnt)
    ```
    
    이중 포문을 이용하여 연속된 구간의 길이를 하나씩 늘려가며, 나누어떨어지는 개수를 카운트하는 방식으로 구간합을 하나씩 체크했다. 그 결과, O(n^2)의 시간 복잡도가 발생했는데. 입력을 고려했을 때 시간 복잡도를 더욱 최적화해야한다. 
    
    > 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 10^6, 2 ≤ M ≤ 10^3)
    > 
    > 
    > 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 10^9)
    > 
    > → 제한시간 1초이기 때문에, 1초에 2,000만 번 연산하는 것을 기준으로 한다면 시간복잡도 최적화가 필요하다.
    > 
    
    <aside>
    📌
    
    **두번째 풀이 : 나머지 합 이용**
    
    </aside>
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dc951d7-030e-4915-afbe-55616c07abf7/9671271f-c71c-4a7c-a981-38ed355501bf/image.png)
    
    → 즉, 나머지가 같은 두개의 시작점과 끝점을 찾으면 그 사이의 구간합은 무조건 나누어 떨어지게 된다! 
    
    ex) [1 2 3 1 2] 의 구간합 [1 3 6 7 9] → 3으로 나눈 나머지의 구간합 [1 0 0 1 0]
    
    여기에서 S[3] - S[0]은 무조건 3으로 나누어 떨어지게 된다. S[3]에 있는 나머지의 값을 S[0]에서 빼주면 0이 되기 때문이다. 따라서 두 값을 선택하는 조합 문제로 바뀌게 된다.
    
    ```java
    import sys
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 구간 합 구하기
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = arr[i] + dp[i]
    
    # 구간 합 나머지 업데이트
    cnt = 0
    for i in range(1, n + 1):
        dp[i] %= m
        if dp[i] == 0:
            cnt += 1  # 나머지가 0인 경우, 길이가 1일때 무조건 성립
    
    # 나머지가 같은 조합의 수를 계산하는 문제로 변형
    for i in range(m):  # m으로 나눈 나머지는 0~m-1 밖에 없음.
        num = 0  # 나머지가 같은 값의 개수
        for j in range(1, n + 1):
            if dp[j] == i:
                num += 1  # 나머지가 같은 값들을 다 더한다.
        if num >= 2:
            cnt += num * (num - 1) / 2  # nC2를 계산
    print(int(cnt))
    ```
    
    해설을 보지 않고 작성한 코드. 여기에서 나머지의 값을 나누고 다시 한번 배열을 순회하며 나머지가 같은 개수를 찾기에 n*m의 시간 복잡도가 발생한다. 
    
    백준에서는 python3에서 시간 초과, pypy3에서는 정답 코드로 풀이되었다.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dc951d7-030e-4915-afbe-55616c07abf7/03c21fe9-ac9b-48b4-aedc-39fe3856daef/image.png)
    
    ```java
    import sys
    
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 구간 합 구하기
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = arr[i] + dp[i - 1]
    
    # 구간 합 나머지 업데이트 (동시에 나머지 배열 초기화도 같이)
    cnt = 0
    rem = [0] * m  # m으로 나눈 나머지는 0~m-1 밖에 없음.
    
    for i in range(n):
        dp[i] %= m
        if dp[i] == 0:
            cnt += 1  # 나머지가 0인 경우, 길이가 1일때 무조건 성립
        rem[dp[i]] += 1  # 해당 나머지를 가진 값 +1
    
    # 나머지가 같은 조합의 수를 계산하는 문제로 변형
    for i in range(m):
        if rem[i] >= 2:
            cnt += rem[i] * (rem[i] - 1) / 2  # nC2를 계산
    print(int(cnt))
    ```
    
    다음과 같이, 부분합을 나눠주는 과정에서 rem의 배열 값을 세팅하면 이중 루프를 단일 루프로 해소할 수 있다. 더 최적화된 코드 완성! 이제 Python3에서도 정답 처리를 받을 수 있었다!
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dc951d7-030e-4915-afbe-55616c07abf7/ec22473f-bb46-4df7-979d-b7fc4a25525a/image.png)


### 투 포인터

리스트에 순차적으로 접근해야 할 때 **두 개의 점의 위치를 기록하면서 처리**하는 알고리즘

정렬되어있는 두 리스트의 합집합에도 사용됨. 병합정렬(merge sort)의 counquer 영역의 기초가 되기도 한다.

**시간 복잡도 O(N)** : 매 루프마다 항상 두 포인터 중 하나는 1씩 증가하고 각 포인터가 n번 누적 증가해야 알고리즘이 끝난다. -> 각각 배열 끝에 다다르는데 O(N) 이라 둘을 합해도 여전히 O(N)이다.

- [[문제] 연속된 자연수의 합 구하기](https://www.acmicpc.net/problem/2018)
    <aside>
    📌
    
    첫번째 풀이 : 시간초과, 메모리 초과
    
    </aside>
    
    ```java
    import sys
    
    input = sys.stdin.readline
    
    # 자연수 받아오기
    n = int(input()) # n이 10,000,000 -> 시간복잡도 O(n)이어야함.
    
    # 자연수의 값까지 만들어지는 배열 찾기. 투포인터로 시작, 끝을 가리키고 하나씩 움직이며 연속된 합이 10인 값 찾기
    # 합 계산이니까 부분합을 써도 될 것 같다. (시작인덱스-(끝 인덱스-1))
    prefix_sum = [
        i * (i + 1) / 2 for i in range(n + 1)
    ]  # 자연수의 합 n(n+1)/2 (0번 인덱스 포함)
    
    cnt = 0
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            if prefix_sum[end] - prefix_sum[start - 1] == n:
                cnt += 1  # 부분 합이 같으면 끝
                break
    
    print(cnt)
    ```
    
    입력이 10,000,000이기 때문에, 1초의 시간 안에서 2천만번의 연산까지 가능하려면 시간복잡도가 O(n)이어야 한다. 따라서 O(N)의 시간 복잡도가 필요하다. 
    
    투포인터를 이중루프로 오해해서 발생한 문제. 투포인터는 while을 이용해 조건을 통해 푼다는 점 기억하기!
    
    <aside>
    📌
    
    두번째 풀이 : 투포인터 이용
    
    </aside>
    
    ```java
    import sys
    
    input = sys.stdin.readline
    
    # 자연수 받아오기
    n = int(input())  # n이 10,000,000 -> 시간복잡도 O(n)이어야함.
    
    # 자연수의 값까지 만들어지는 배열 찾기. 투포인터로 시작, 끝을 가리키고 하나씩 움직이며 연속된 합이 n인 값 찾기
    arr = [i for i in range(n + 1)]  # n인 경우는 고려하지 않아도 됨 (스스로 만족)
    
    # 자기 자신일때 미리 카운트
    cnt = 1
    # 투 포인터 인덱스 초기화
    start = 1
    end = 1
    sum = 1  # 시작 합 1
    
    # 끝 인덱스부터 하나씩 늘려나가며 합을 계산. 합이 n인 경우 카운트 세고 시작 인덱스 이동 (sum 초기화 필요)
    while end != n:
        if sum < n:  # 합 만족 X -> 끝 인덱스 이동
            end += 1
            sum += arr[end]
        elif sum == n:  # 합 만족 -> 카운트 계산
            cnt += 1
            end += 1
            sum += arr[end]
        else:  # 합보다 큼 -> 시작 인덱스 이동
            sum -= arr[start]
            start += 1
    
    print(cnt)
    ```
    
    → Python3에서는 메모리 초과, Pypy3에서는 통과했다. 그 이유를 알아보기 위해 확인을 했더니… 
    
    메모리 제한은 32 MB인데 반해, `n = 10,000,000`이므로 배열 `arr`는 0부터 10,000,000까지의 값을 저장하는 리스트가 된다. 리스트의 크기는 `n + 1`이고, 각 요소는 4바이트(정수형 메모리 크기)로 할당되므로 이 리스트는 약 40MB 이상의 메모리를 차지하게 되어 메모리 초과가 발생한 것!! 
    
    메모리 제한을 고려했을 때, 배열을 만들지 않고 투 포인터 알고리즘을 개선하는 방법으로 메모리 사용을 줄일 수 있다. 사실상 배열이 없어도 `start`와 `end` 포인터만으로 충분히 합을 계산할 수 있기 때문에 배열을 명시적으로 생성할 필요는 없다.
    
    연속되는 자연수를 리스트로 나타내야 한다는 강박에 빠져서 발생한 문제였다.. 어차피 인덱스의 값이 자연수의 값과 똑같기 때문에, `arr`을 선언하지 않아도 인덱스만을 이용하여 풀 수 있었던 문제.
    
    <aside>
    📌
    
    개선된 코드
    
    </aside>
    
    ```java
    import sys
    
    input = sys.stdin.readline
    
    # 자연수 받아오기
    n = int(input())  # n이 10,000,000 -> 시간복잡도 O(n)이어야함.
    
    # 자기 자신일때 미리 카운트
    cnt = 1
    # 투 포인터 인덱스 초기화
    start = 1
    end = 1
    sum = 1  # 시작 합 1
    
    # 끝 인덱스부터 하나씩 늘려나가며 합을 계산. 합이 n인 경우 카운트 세고 시작 인덱스 이동 (sum 초기화 필요)
    while end != n:
        if sum < n:  # 합 만족 X -> 끝 인덱스 이동
            end += 1
            sum += end
        elif sum == n:  # 합 만족 -> 카운트 계산
            cnt += 1
            end += 1
            sum += end
        else:  # 합보다 큼 -> 시작 인덱스 이동
            sum -= start
            start += 1
    
    print(cnt)
    ```

- [[문제] 주몽의 명령](https://www.acmicpc.net/problem/1940)
  ```python
  import sys

  input = sys.stdin.readline

  n = int(input())  # 15,000 (재료의 개수)
  m = int(input())  # 10,000,000 (갑옷 충족 번호)
  arr = list(map(int, input().split()))  # 재료의 고유한 번호
  arr.sort()  # 오름차순 정렬

  start = 0  # 시작 인덱스
  end = n - 1  # 끝 인덱스
  cnt = 0

  # 시작 인덱스와 끝 인덱스의 합을 비교하며 값을 줄여나가기
  while start != end:
      sum = arr[start] + arr[end]
      if sum == m:  # 현재 합이 같으면
          cnt += 1
          end -= 1
          start += 1
      elif sum > m:  # 현재 합이 크면 -> 큰 값 - 1
          end -= 1
      else:  # 현재 합이 작으면 -> 작은 값 +1
          start += 1

  print(cnt)
  ```
  코드를 작성할 때, 머릿속으로만 생각하는 것보다 직접 메모도 하고 계산하는 것이 무엇보다 중요하다는 것을 다시금 깨달았다. 직접 코드를 판단하고 이동 과정을 구체화해봐야 풀이와 조건을 어떻게 진행할 지 가닥이 잡히는 것 같다.
  기존 투포인터와 크게 다르지 않은 문제라 무난하게 풀 수 있었다.
  하지만 `if sum == m:` 조건에서 포인터를 어떻게 움직일까 고민을 하다가, 처음에는 start만 이동을 시켰는데 어차피 sum이 같아지는 순간을 찾을 것이고, 한 쪽만 움직인다면 어차피 다시 반복을 해야 하기 때문에 시작과 끝 인덱스를 둘 다 바꿔주는 것이 좋다는 점을 깨달았다.

### 슬라이딩 윈도우

투포인터처럼 구간을 훑으면서 지나간다는 공통점이 있으나 슬라이딩 윈도우는 **어느 순간에도 구간의 넓이가 동일하다**는 차이점이 있다.

- [[문제] 좋은 수 구하기](https://www.acmicpc.net/problem/1253)
    <aside>
    📌
    
    변형된 문제 : 수의 위치가 다르면 값이 같아도 다른 수이다. (해당 조건 삭제하고 슬라이딩 윈도우로 풀이)
    
    </aside>
    
    ```python
    import sys
    input = sys.stdin.readline
    
    n = int(input())  # 수의 개수 (2,000)
    arr = list(map(int, input().split()))
    arr.sort()
    
    # 다른 두 수의 합으로 표현되는 수가 있다면 좋은 수라고 함!
    cnt = 0
    for target in range(2, n):  # target idx는 2부터 시작(0,1이 시작 인덱스)
        start = 0
        end = target - 1
        while start < end:
            sum = arr[start] + arr[end]
            if sum == arr[target]:  # 현재 합이 같으면 -> 좋은 수로 판단하고 다른 타겟!
                cnt += 1
                break
            elif sum > arr[target]:  # 현재 합이 크면 -> 큰 값 - 1
                end -= 1
            else:  # 현재 합이 작으면 -> 작은 값 +1
                start += 1
    
    print(cnt)
    ```

- [문제] [DNA 비밀번호](https://www.acmicpc.net/problem/12891)
    <aside>
    📌
    
    첫번째 풀이 : 시간복잡도 초과
    
    </aside>
    
    ```python
    s, p = map(int, input().split())  # 문자열 길이 S, 부분문자열의 길이 P
    string = input()  # DNA 문자열
    str_arr = list(
        map(int, input().split())
    )  # 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수
    
    # 슬라이딩 윈도우 (i는 시작 인덱스)
    cnt = 0
    for i in range(s - p + 1):
        target = string[i : i + p]
        if str_arr[0] > target.count("A"):
            continue
        if str_arr[1] > target.count("C"):
            continue
        if str_arr[2] > target.count("G"):
            continue
        if str_arr[3] > target.count("T"):
            continue
        cnt += 1
    
    print(cnt)
    ```
    
    단순하게 생각했을 때, 부분 문자열을 매번 만들어서 그 안에 있는 A, C, G, T의 개수를 세면 되는 것 아닌가 라고 생각을 했다. 하지만  (1 ≤ |P| ≤ |S| ≤ 1,000,000)라는 조건에서, O(n)으로 문제를 풀어야 했는데, count의 시간복잡도는 n이기 때문에 O(n^2)으로 시간 초과가 발생했다. 
    
    그렇다면 어떻게 부분 문자열에 있는 알파벳을 비교할 수 있을까? 
    
    이를 해결하기 위해 알파벳의 숫자를 따로 세어 최소 개수와 비교하는 식으로 문제를 풀어보려고 한다. 
    
    <aside>
    📌
    
    두번째 풀이 : 문자열의 숫자를 비교한 풀이
    
    </aside>
    
    ```python
    s, p = map(int, input().split())  # 문자열 길이 S, 부분문자열의 길이 P
    string = input()  # DNA 문자열
    min_str = list(
        map(int, input().split())
    )  # 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수
    current_str = [0] * 4
    cnt = 0
    
    def add(c):  # 문자가 들어왔을 때 계산하는 함수
        global current_str
        if c == "A":
            current_str[0] += 1
        elif c == "C":
            current_str[1] += 1
        elif c == "G":
            current_str[2] += 1
        else:
            current_str[3] += 1
    
    def sub(c):  # 문자가 빠질 때 계산하는 함수
        global current_str
        if c == "A":
            current_str[0] -= 1
        elif c == "C":
            current_str[1] -= 1
        elif c == "G":
            current_str[2] -= 1
        else:
            current_str[3] -= 1
    
    def check():  # 최소 값을 만족시키는지 확인
        global cnt, current_str, min_str
        if (
            current_str[0] >= min_str[0]
            and current_str[1] >= min_str[1]
            and current_str[2] >= min_str[2]
            and current_str[3] >= min_str[3]
        ):
            cnt += 1
    
    for i in range(p):  # 부분 문자열 개수 초기화
        if string[i] == "A":
            current_str[0] += 1
        elif string[i] == "C":
            current_str[1] += 1
        elif string[i] == "G":
            current_str[2] += 1
        else:
            current_str[3] += 1
    
    check()
    
    # 슬라이딩 윈도우
    for i in range(1, s - p + 1):
        add(string[i + p - 1])  # 이후 문자열 추가
        sub(string[i - 1])  # 이전 문자열 제거
        check()
    print(cnt)
    ```
    
    슬라이딩 윈도우를 잡아놓고, 해당 문자열 안에 있는 수를 하나씩 세서 비교하여 문제를 해결하였다. 이런 아이디어 하나하나가 중요한 듯.
    
    그리고, for문 사용시에 시작 인덱스를 기준으로 하다 보니까 계산이 힘들었다.. 디버깅을 이용하면 확인할 수 있기는 하지만 디버깅 허용 안되는 문제들도 있으니 꼭 작은 테스트케이스를 바탕으로 문제 푸는 것을 익히도록 하자!!

- [[문제] 최솟값 찾기1](https://www.acmicpc.net/problem/11003)
  **문제 풀이 아이디어**
  이 문제는 단순히 슬라이딩 윈도우를 움직이는 것 뿐 아니라, 최솟값을 기록해야 한다. 하지만, 최솟값만을 단순히 기억하면 슬라이딩 윈도우가 움직여버렸을 때 최솟값이 어떻게 변화했는지 찾을수가 없다. (인덱스가 기록되지 않기 때문에.. 만약 인덱스를 기록한다고 하더라도 움직여버리는 순간 두번째로 작은 값이 최솟값이어야 하는데 매번 찾을 수 없다)
  이 문제의 n값이 5,000,000이기 때문에 min함수를 사용해버리면 O(n^2)의 시간복잡도가 되어 시간 초과가 발생할 것이다.
  → 이를 해결하기 위해, 덱 구조에 인덱스와 값을 저장하며 최솟값을 기록하는 느낌으로 계산을 진행하겠다.
  ```python
  from collections import deque
  import sys

  input = sys.stdin.readline

  n, l = map(int, input().split())
  arr = list(map(int, input().split()))
  d = deque()  # 최솟값을 기록할 덱

  for i in range(n):
      # 최솟값 업데이트 - (덱에 값이 있을 떄) 덱의 오른쪽에서부터 본인보다 작은 값 삭제
      while d and d[-1][1] > arr[i]:
          d.pop()
      d.append([i, arr[i]])  # 본인 값 추가
      # 슬라이딩 윈도우 크기 조사
      if d[0][0] <= i - l:  # 범위가 아닌 값 삭제
          d.popleft()
      print(d[0][1], end=" ")  # 현재 최솟값 출력
  ```
  코드 자체는 간결하지만, 최솟값을 계속 기록해야 할 때 어떻게 풀이해야 하는지를 위한 아이디어가 중요했던 문제. (자료구조는 정말정말 중요하다!)
  인덱스와 크기를 바탕으로 덱을 구성하는 아이디어를 꼭 가지고가자!

### 덱(Deque, Double Ended Queue)

- 덱(Dequeue)은 데이터 값을 저장하는 기본적인 구조로, 일차원의 선형 자료구조이다.
- 덱은 스택(Stack)과 큐(Queue)의 연산을 모두 지원하는 자료구조로, 양 끝에서 모두 삽입과 삭제가 가능한 큐라고 생각하면 된다.
- 나머지 부가적인 덱의 길이를 반환하는 연산이나 덱이 비어있는지 확인하는 연산 등은 스택과 큐에 구현되어 있는 연산들과 유사하게 구현된다.

`collections`라는 모듈에 `deque`라는 클래스로 이미 구현되어 있다. 여기서 특별한 점은 양 끝에서 삽입과 삭제를 할 수 있어야 하므로 양방향 연결리스트(Doubly Linked List)로 구성되어 있다. 단순히 값을 삽입하고 삭제하는 용도로만 활용할 때는 `O(1)`만큼의 시간밖에 할애되지 않기 때문에 아주 효율적이다.

```python
from collections import deque

d = deque()
print(type(d))  # <class 'collections.deque'>

# 스택이나 큐처럼 덱의 오른쪽에서 요소 삽입 : append
for i in range(10):
    d.append(i)
print(d)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 덱의 왼쪽에서 요소 삽입 : appendleft
d.appendleft(10)
print(d)  # deque([10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 덱 중간에 요소 삽입 : insert
d.insert(5, 11)
print(d)  # deque([10, 0, 1, 2, 3, 11, 4, 5, 6, 7, 8, 9])

# 덱 왼쪽/오른쪽에 iterable한 객체를 통째로 append 하여 연장시키는 연산 : extendleft / extend
d.extend([0, 0, 0])
print(d)  # deque([10, 0, 1, 2, 3, 11, 4, 5, 6, 7, 8, 9, 0, 0, 0])

d.extendleft([0, 0, 0])
print(d)  # deque([0, 0, 0, 10, 0, 1, 2, 3, 11, 4, 5, 6, 7, 8, 9, 0, 0, 0])

# 스택처럼 덱의 오른쪽에서 요소 삭제 : pop
for i in range(10):
    d.pop()
print(d)  # deque([0, 0, 0, 10, 0, 1, 2, 3])

# 큐처럼 덱의 왼쪽에서 요소 삭제 : popleft
for i in range(3):
    d.popleft()
print(d)  # deque([10, 0, 1, 2, 3])

# 작업을 완료한 후에는 일반적인 리스트처럼 이용할 수도 있다
print(list(d))  # [10, 0, 1, 2, 3]
```
