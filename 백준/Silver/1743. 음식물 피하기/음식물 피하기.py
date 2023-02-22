import sys
sys.setrecursionlimit(10**5)
result = []
M, N, number = map(int, sys.stdin.readline().split())
#가로 = N 세로 = M
data = [[0 for _ in range(N)]for _ in range(M)]

for _ in range(number):
  A, B = map(int, sys.stdin.readline().split())
  data[A-1][B-1] = 1

def dfs(x, y):
  if x<0 or x>= M or y<0 or y>= N: return
  if data[x][y] == 0: return
  global stack
  if data[x][y] == 1: stack +=1 
  data[x][y] = 0
  dfs(x+1, y)
  dfs(x, y+1)
  dfs(x-1, y)
  dfs(x, y-1)

for a in range(M):
  for b in range(N):
    if data[a][b] == 1:
      stack = 0
      dfs(a, b)
      result.append(stack)

print(max(result))