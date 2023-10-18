import sys
sys.setrecursionlimit(10**6)
data = []
result_sheep, result_wolf = 0, 0

def DFS(x, y) :
  if x<0 or x>=N or y<0 or y>=M or visited[x][y] == 1 : return
  visited[x][y] = 1
  global wolf, sheep
  if data[x][y] == '#' : return
  if data[x][y] == 'v' : wolf += 1
  if data[x][y] == 'k' : sheep += 1
  DFS(x+1, y)
  DFS(x, y+1)
  DFS(x-1, y)
  DFS(x, y-1)

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
  data.append(list(map(str, sys.stdin.readline().strip())))

visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N) :
  for j in range(M) :
    if visited[i][j] == 0 :
      sheep, wolf = 0, 0
      DFS(i, j)
      if sheep > wolf : result_sheep += sheep
      else : result_wolf += wolf

print(result_sheep, result_wolf)