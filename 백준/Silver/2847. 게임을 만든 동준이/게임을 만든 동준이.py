import sys

data = []
result = 0
n = int(sys.stdin.readline())
for _ in range(n):
    data.append(int(sys.stdin.readline()))

for i in range(len(data) - 1, 0, -1):
    if data[i] > data[i - 1]: continue
    while data[i] <= data[i - 1]:
        result += 1
        data[i - 1] -= 1

print(result)