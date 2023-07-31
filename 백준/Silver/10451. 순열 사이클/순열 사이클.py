import sys

def dfs(data, N, visited):
    visited[N] = 1
    if visited[data[N]-1] == 0 :
      dfs(data, data[N]-1, visited)

cycle = int(sys.stdin.readline())

for l in range(cycle) :
  N = int(sys.stdin.readline())
  data = list(map(int,sys.stdin.readline().split()))
  visited = [0] * N
  result = 0

  for i in range(N) :
    if visited[i] == 0:
      dfs(data, i, visited)
      result += 1
      
  print(result)