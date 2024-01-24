import sys
data = []
result = 1

n, m = map(int, sys.stdin.readline().split())
for _ in range(n) :
    data.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(n) :
    for x in range(m):
        if x == m-1 : continue
        for y in range(x+1, m) :
            if data[i][x] == data[i][y] :
                if i+y-x >= n : continue
                if data[i+y-x][x] == data[i][x] and data[i+y-x][y] == data[i][x] :                    result = max(result, (y-x+1)**2)

print(result)