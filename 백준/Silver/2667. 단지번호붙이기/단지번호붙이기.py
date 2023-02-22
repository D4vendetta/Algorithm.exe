import sys
data, result = [], []

N = int(sys.stdin.readline())
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().strip())))

def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=N : return
    if data[x][y] == 0 : return
    data[x][y] = 0
    global count
    count += 1
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)

for a in range(N):
    for b in range(N):
        count = 0
        if data[a][b] == 1:
            dfs(a, b)
            result.append(count)

print(len(result))
result.sort()
for k in result:
    print(k)