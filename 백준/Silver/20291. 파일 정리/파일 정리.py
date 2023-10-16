import sys

N = int(sys.stdin.readline())
data = {}

for _ in range(N) :
    A, B = map(str, sys.stdin.readline().strip().split("."))
    if B in data : 
        data[B] += 1
    else : 
        data[B] = 1

data_list = sorted(data.items(), key=lambda x:x[0])

for i in data_list:
    print(*i)