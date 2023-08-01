import sys

data = []
result = 0
N, M = map(int, sys.stdin.readline().split()) #N = 세로 M = 가로
for _ in range(N):
  data.append(list(map(str, sys.stdin.readline().strip())))
visited = [[0 for j in range(M)] for i in range(N)]

def dfs(x, y, panel) :
  if x >= N or y >= M or visited[x][y] == 1 or data[x][y] != panel : return
  visited[x][y] = 1
  if panel == '-' : dfs(x, y+1, panel)
  if panel == '|' : dfs(x+1, y, panel)

for j in range(N) :
  for k in range(M) :
    if visited[j][k] == 0:
      dfs(j, k, data[j][k])
      result += 1
      
print(result)