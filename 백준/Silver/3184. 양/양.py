import sys
sys.setrecursionlimit(10**5)
wolf, sheep = 0, 0

R, C = map(int, sys.stdin.readline().split())
graph = []
#R = X = 세로, C = Y = 가로
for _ in range(R):
  graph.append(list(map(str, sys.stdin.readline().strip())))

def dfs(x, y, w, s):
  if x < 0 or x >= R or y < 0 or y >= C or graph[x][y] == '#' or graph[x][y] == 1 : return
  global wof
  global shp
  if graph[x][y] == 'v' : 
    wof = w + 1
  if graph[x][y] == 'o' : 
    shp = s + 1
  graph[x][y] = 1
  dfs(x+1, y, wof, shp)
  dfs(x, y+1, wof, shp)
  dfs(x-1, y, wof, shp)
  dfs(x, y-1, wof, shp)

for a in range(R):
  for b in range(C):
    wof = shp = 0
    if graph[a][b] == 1 or graph[a][b] == '#': continue
    dfs(a, b, 0, 0)
    if shp == 0 and wof == 0 : continue
    elif shp > wof : sheep += shp
    else : wolf += wof
      
print(sheep, wolf)