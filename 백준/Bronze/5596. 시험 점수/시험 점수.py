import sys

data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))
result1 = sum(data1)
result2 = sum(data2)

print(max(result1, result2))