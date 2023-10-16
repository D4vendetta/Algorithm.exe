import sys

N, M = map(int, sys.stdin.readline().split())
data = {}
result = 0

for j in range(N) :
    input_value = sys.stdin.readline()
    data[input_value] = j

for k in range(M) :
    qustion = sys.stdin.readline()
    try :
        data[qustion] 
        result += 1 
    except : continue

print(result)