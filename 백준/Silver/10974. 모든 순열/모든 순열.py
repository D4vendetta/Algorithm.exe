from itertools import permutations
line = []
N = int(input())

for i in range(1, N+1):
    line.append(i)

result = list(permutations(line, N))

for i in range(len(result)) :
    print(*result[i])