#1 = 땅, 0 = 바다
#visited -> 0으로 변환
import sys
sys.setrecursionlimit(10**4)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 : break
    data = []
    data.clear()
    count = 0
    for i in range(h):
        data.append(list(map(int,sys.stdin.readline().split())))

    def dfs(x, y) :
        if x <= -1 or x >= h or y <= -1 or y>= w or data[x][y] == 0:
            return
        else :
            data[x][y] = 0
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x+1, y+1)
            dfs(x-1, y-1)
            dfs(x+1, y-1)
            dfs(x-1, y+1)
    for a in range(h):
        for b in range(w):
            if data[a][b] == 1:
                dfs(a, b)
                count += 1

    print(count)