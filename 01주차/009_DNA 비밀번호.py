S, P = map(int, input().split())
dna = input()
minCounts = list(map(int, input().split()))

currentCounts = [0] * 4
checkValid = 0

indexOfChar = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

for i in range(P):
    currentCounts[indexOfChar[dna[i]]] += 1
    
def is_valid():
    for i in range(4):
        if currentCounts[i] < minCounts[i]:
            return False
    return True

if is_valid():
    checkValid += 1
    
for i in range(P, S):
    currentCounts[indexOfChar[dna[i]]] += 1
    currentCounts[indexOfChar[dna[i - P]]] -= 1
    
    if is_valid():
        checkValid += 1
        
print(checkValid)
