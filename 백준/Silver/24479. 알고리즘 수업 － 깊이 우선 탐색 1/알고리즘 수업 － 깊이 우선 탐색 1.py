import sys
sys.setrecursionlimit(10**5)
N, M, R = map(int, sys.stdin.readline().split())
visited = [0]*(N+1)
graph = [[] for i in range(N+1)]
stack = 1

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for j in range(N+1):
    graph[j].sort()

def dfs(k):
    global stack
    visited[k] = stack
    stack += 1
    for j in graph[k]:
        if visited[j] == 0:
            dfs(j)

dfs(R)
for z in visited[1:]:
    print(z)