import sys
from collections import deque

graph = []
N, M = map(int, sys.stdin.readline().split())
for _ in range(N) :
  v = list(map(int, sys.stdin.readline().rstrip()))
  graph.append(v)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y) :
  queue = deque()
  queue.append((x, y))

  while queue :
    x, y = queue.popleft()

    for i in range(4) :
      nx, ny = x + dx[i], y + dy[i] 

      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
  return graph[N-1][M-1]

print(bfs(0, 0))