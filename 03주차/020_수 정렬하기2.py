import sys

n = int(sys.stdin.readline())
numbers = []

for i in range(n):
    number = int(sys.stdin.readline())
    numbers.append(number)

numbers.sort()

for number in numbers:
    print(number)
