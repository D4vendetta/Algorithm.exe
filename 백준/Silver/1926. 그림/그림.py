import sys
sys.setrecursionlimit(10**6)
# N * M
M, N = map(int, sys.stdin.readline().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    if x<0 or x>=M or y<0 or y>=N : return
    if graph[x][y] == 0 : return
    graph[x][y] = 0
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)
    global size
    size += 1

count, result= 0, 0
for a in range(M):
    for b in range(N):
        size = 0
        if graph[a][b] == 1:
            dfs(a, b)
            count += 1
            result = max(result, size)
            
if count == 0 : result = 0
print(count)
print(result)