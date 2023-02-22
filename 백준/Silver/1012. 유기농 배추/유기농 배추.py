import sys
sys.setrecursionlimit(10**5)
testcase = int(sys.stdin.readline())

def dfs(x, y):
  if x<0 or x>=M or y<0 or y>= N: return
  if data[x][y] == 0: return
  data[x][y] = 0
  dfs(x+1, y)
  dfs(x, y+1)
  dfs(x-1, y)
  dfs(x, y-1)

while testcase != 0:
  count = 0
  N, M, K = map(int, sys.stdin.readline().split())
  data = [[0 for _ in range(N)]for _ in range(M)]
  for _ in range(K):
    A, B = map(int, sys.stdin.readline().split())
    data[B][A] = 1
    
  for a in range(M):
    for b in range(N):
      if data[a][b] == 1:
        dfs(a, b)
        count += 1
  print(count)
  testcase -= 1