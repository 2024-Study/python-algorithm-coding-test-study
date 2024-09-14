import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))  # 목표 스택

stack = []
pointer = 0
num = 1
while pointer != n:  # 자연수를 바탕으로 스택쌓기
    if len(stack) == 0 and num <= n:  # 스택이 비어있다면?
        stack.append(num)
        num += 1
        print("+")
    if stack[-1] != arr[pointer]:  # push
        stack.append(num)
        num += 1
        print("+")
    else:  # pop
        pointer += 1
        print("-")
        stack.pop()
