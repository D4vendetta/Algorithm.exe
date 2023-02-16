from itertools import permutations

A, B = map(int, input().split())
data = []

for i in range(1, A+1):
    data.append(i)

result = list(permutations(data, B))

for j in result:
    print(*j)