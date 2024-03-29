import sys

N, M = map(int, sys.stdin.readline().split())
data = {}

for _ in range(N):
    temp = sys.stdin.readline().rstrip('\n')
    if len(temp) < M : continue
    if temp not in data :
        data[temp] = 1
    else :
        data[temp] += 1

result = sorted(data.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
        
for i in result:
    print(i[0])