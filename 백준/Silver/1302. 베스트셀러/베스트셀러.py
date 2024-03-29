import sys

n = int(sys.stdin.readline())
data ={}

for _ in range(n):
    temp = sys.stdin.readline().rstrip('\n')
    if temp in data:
        data[temp] += 1
    else :
        data[temp] = 1

result = sorted(data.items(), key = lambda x:(-x[1], x[0]))
print(result[0][0])