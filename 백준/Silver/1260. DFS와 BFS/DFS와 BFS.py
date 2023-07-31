import sys
from collections import deque

def dfs(N) :
  visited[N] = 1
  DFS_result.append(N)
  for k in graph[N] :
     if visited[k] == 0:
        dfs(k)

def bfs(N) :
  queue = deque([N])
  visited[N] = 1
  while queue :
     k = queue.popleft()
     BFS_result.append(k)
     for j in graph[k] :
        if visited[j] == 0:
           queue.append(j)
           visited[j] = 1

DFS_result = []
BFS_result = []

#간선 및 그래프 입력
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for z in range(N+1) :
   graph[z].sort()

visited = [0]*(N+1)
dfs(V)
visited = [0]*(N+1)
bfs(V)
print(*DFS_result)
print(*BFS_result)