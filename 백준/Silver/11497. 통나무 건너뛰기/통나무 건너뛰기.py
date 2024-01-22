import sys

case = int(sys.stdin.readline())
for i in range(case) :
    result = 0
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    for j in range(2, n) :
        result = max(result, abs(data[j] - data[j-2]))
    print(result)