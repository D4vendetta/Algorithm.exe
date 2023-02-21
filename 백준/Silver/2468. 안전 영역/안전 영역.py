import sys
sys.setrecursionlimit(10**5)
data = []
result, rain = 0, 0

N = int(sys.stdin.readline())
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

max_rain = max(map(max, data))
#------구현
def dfs(x, y, rain):
    if x < 0 or x >= N or y < 0 or y >= N or data[x][y] <= rain or visited[x][y] == 1 : return
    visited[x][y] = 1
    dfs(x+1, y, rain)
    dfs(x, y+1, rain)
    dfs(x-1, y, rain)
    dfs(x, y-1, rain)

while rain != max_rain:
    visited =  [[0 for _ in range(N)] for _ in range(N)]
    count = 0
    for a in range(N):
        for b in range(N):
            if data[a][b] > rain and visited[a][b] == 0:
                dfs(a, b, rain)
                count += 1
    rain += 1
    result = max(result, count)

print(result)