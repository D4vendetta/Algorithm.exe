import sys

N, M = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

result = (A-B)
print(len(result))
if len(result) != 0:
    result = list(result)
    result.sort()
    print(*result)