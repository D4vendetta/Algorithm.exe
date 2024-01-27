import sys

n, l = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
result = 0
tape = 0
data.sort()

for i in range(n) :
    if data[i] <= tape :
        continue
    else : 
        result += 1
        tape = int(data[i])-1+l

print(result)