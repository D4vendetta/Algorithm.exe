from itertools import combinations
data = []

M, N = map(int, input().split())
for i in range(1, M+1):
    data.append(i)

result = list(combinations(data, N))

for j in result:
    print(*j)