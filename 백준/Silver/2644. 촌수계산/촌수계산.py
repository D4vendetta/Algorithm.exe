import sys

N = int(sys.stdin.readline())
X, Y = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

visited = [0]*(N+1)
graph = [[]for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def dfs(z, count):
    visited[z] = count
    if z == Y : return
    for c in graph[z]:
        if visited[c] == 0:
            dfs(c, count+1)

dfs(X, 0)
if visited[Y] == 0: print(-1)
else : print(visited[Y])