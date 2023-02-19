import sys
sys.setrecursionlimit(10**6)
count = 0

def dfs(V):
    visited[V] = 1
    for k in graph[V]:
        if visited[k] == 0:
            dfs(k)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)
visited[0] = 1

#그래프 생성
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]

dfs(1)
#방문
while 0 in visited:
    z = visited.index(0)
    dfs(z)
    count += 1

print(count+1)