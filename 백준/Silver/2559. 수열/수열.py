import sys

N, M = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
result = float('-inf')
curr_sum, start = 0, 0

for end, val in enumerate(data):
    curr_sum += val
    if end - start + 1  == M:
        result = max(result, curr_sum)
        curr_sum -= data[start]
        start += 1
print(result)