import sys
sys.setrecursionlimit(10**5)
M, N, K = map(int, sys.stdin.readline().split())
result_size = []
size, count = 0, 0

data = [[0 for j in range(M)] for i in range(N)]
for _ in range(K):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  for i in range(x1, x2):
    for j in range(y1, y2):
      if i >= N or j >= M : continue
      data[i][j] = 1
      
def dfs(z, y, s_size):
  if z < 0 or z >= N or y <0 or y>= M or data[z][y] == 1 : return
  global size
  if data[z][y] == 0:
    data[z][y] = 1
    size = s_size + 1
    dfs(z+1, y, size)
    dfs(z, y+1, size)
    dfs(z-1, y, size)
    dfs(z, y-1, size)

for a in range(N):
  for b in range(M):
    if data[a][b] == 1: continue
    dfs(a, b, 0)
    count += 1
    result_size.append(size)

result_size.sort()
print(count)
print(*result_size)