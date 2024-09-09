n = int(input())
num = input()
print(sum(list(map(int, num))))
# map 객체는 이터레이터이기 때문에 print(sum(map(int, num)))로 풀어도 가능하다!
