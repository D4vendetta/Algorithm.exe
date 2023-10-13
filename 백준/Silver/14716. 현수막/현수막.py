import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

data = []
result = 0
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]

def dfs(x, y) :
  if x<0 or x>=N or y<0 or y>=M or visited[x][y] == 1 or data[x][y] == 0 : return
  visited[x][y] = 1
  dfs(x, y+1)
  dfs(x, y-1)
  dfs(x+1, y)
  dfs(x+1, y-1)
  dfs(x+1, y+1)
  dfs(x-1, y)
  dfs(x-1, y+1)
  dfs(x-1, y-1)

for j in range(N):
   for k in range(M) : 
      if data[j][k] == 1 and visited[j][k] == 0:
         result = result + 1
         dfs(j, k)

print(result)