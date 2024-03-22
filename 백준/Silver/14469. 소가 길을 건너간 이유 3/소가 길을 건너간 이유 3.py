import sys

n = int(sys.stdin.readline())
result = 0
data = []
for _ in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))
data.sort(key = lambda x:x[0])

for k in data :
    if result <= k[0] :
        result = k[0] + k[1]
    else :
        result = result + k[1]

print(result)
