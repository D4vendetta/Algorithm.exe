import sys
data =[]
result = []

from itertools import combinations_with_replacement
N, M = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    data.append(i)

result = list(combinations_with_replacement(data, M))
for k in result:
    print(*k)