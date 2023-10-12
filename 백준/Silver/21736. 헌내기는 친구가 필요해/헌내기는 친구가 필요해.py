import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
friend = 0

graph = []
for j in range(N):
  graph.append(list(map(str, sys.stdin.readline().strip())))

for a in range(N) :
   for b in range(M) :
      if graph[a][b] == "I": 
        status_X = a
        status_Y = b
        break

visited = [[0 for _ in range(M)] for _ in range(N)]

def dfs(x, y):
    global friend
    if x<0 or x>=N or y<0 or y>=M or visited[x][y] == 1 or graph[x][y] == 'X' : return
    if graph[x][y] == 'P' : friend = friend+1
    visited[x][y] = 1
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x, y-1)

dfs(status_X, status_Y)

print("TT") if friend == 0 else print(friend)