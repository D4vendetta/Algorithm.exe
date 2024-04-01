import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = [[] for _ in range(N + 1)]

#data 친구관계 간선 연결
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  data[a].append(b)
  data[b].append(a)

#bfs 기능 구현
def bfs(x):
  result = 0
  queue = deque()
  queue.append([x, 0])
  visited = []
  while queue:
    y = queue.popleft()
    if y[0] in visited : continue
    visited.append(y[0])
    result += y[1]
    for i in data[y[0]]:
      if i not in visited:
        queue.append([i, y[1] + 1])
  return result

#N명에 대해 bfs 실행
bacon = 10000000
for j in range(1, N + 1):
  if bacon > bfs(j) :
    bacon = bfs(j)
    answer = j
print(answer)