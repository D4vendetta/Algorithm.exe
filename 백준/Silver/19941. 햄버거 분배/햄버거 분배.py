import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(str, sys.stdin.readline().rstrip()))
result = 0

for i in range(len(data)) :
    if data[i] == 'P' :
        for j in range(k, -k-1, -1):
            if i-j < 0 or i-j >= len(data) : continue
            if data[i-j] =='H' :
                data[i-j] = 'U'
                result += 1
                break

print(result)