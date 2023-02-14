import sys
from itertools import permutations

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
arr = list(permutations(data, N))
result = 0

for i in range(len(arr)):
    pre_result = 0
    for j in range(0, N-1):
        pre_result += abs(arr[i][j] - arr[i][j+1])
    result = max(result, pre_result)

print(result)