import sys
data = []
power_w, power_b = 0, 0

N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
  data.append(list(map(str, sys.stdin.readline().strip())))
  
visited = [[0 for _ in range(N)] for _ in range(M)] 

def dfs(x, y, type):
  if x >= M or x<0 or y>=N or y<0 or visited[x][y] == 1 or data[x][y] != type: return
  visited[x][y] = 1
  global stack
  stack += 1
  dfs(x+1, y, type)
  dfs(x, y+1, type)
  dfs(x-1, y, type)
  dfs(x, y-1, type)

for a in range(M):
  for b in range(N):
    stack = 0
    dfs(a, b, data[a][b])
    if data[a][b] == 'W': power_w+= stack**2
    else : power_b += stack**2

print(power_w, power_b)