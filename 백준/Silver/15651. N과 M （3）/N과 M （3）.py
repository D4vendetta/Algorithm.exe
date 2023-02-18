import itertools
from itertools import product

M, N = map(int, input().split())
line = []
for i in range(1, M+1):
    line.append(i)

result = itertools.product(line, repeat = N)

for i in result:
    print(*i)