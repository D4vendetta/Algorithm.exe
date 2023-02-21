import sys
sys.setrecursionlimit(10**5)
data = []
count1, count2 = 0, 0

N = int(sys.stdin.readline())
for _ in range(N):
    data.append(list(map(str, sys.stdin.readline().strip())))
visited = [[0 for _ in range(N)] for _ in range(N)]

#영역 세기
def dfs(x, y, color):
    if x<0 or x>=N or y<0 or y>=N or visited[x][y] == 1 or data[x][y] != color : return
    visited[x][y] = 1
    dfs(x+1, y, color)
    dfs(x, y+1, color)
    dfs(x-1, y, color)
    dfs(x, y-1, color)

#변경 전 카운트
for q in range(N):
    for w in range(N):
        if visited[q][w] == 0:
            dfs(q, w, data[q][w])
            count1 += 1

#G -> R 변경
for a in range(N):
    for b in range(N):
        if data[a][b] == 'G':
            data[a][b] = 'R'

#변경 후 카운트
visited = [[0 for _ in range(N)] for _ in range(N)]
for h in range(N):
    for j in range(N):
        if visited[h][j] == 0:
            dfs(h, j, data[h][j])
            count2 += 1

print(count1, count2)