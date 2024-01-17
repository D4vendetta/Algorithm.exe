import sys

n = sys.stdin.readline()
data = list(map(int, sys.stdin.readline().split()))

buy = 100000000000
result = 0
for i in range(len(data)) :
    if data[i] < buy : buy = data[i]
    elif data[i] > buy : result = max(result, data[i]-buy)

print(result)