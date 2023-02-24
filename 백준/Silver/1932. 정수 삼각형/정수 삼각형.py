import sys
graph = []

N = int(sys.stdin.readline())
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
  stack = 0
  for j in range(i+1):
    if j == 0 : graph[i][j] = graph[i-1][0] + graph[i][j]
    elif j == i : graph[i][j] = graph[i-1][i-1] + graph[i][j]
    else : graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j]

print(max(graph[N-1]))