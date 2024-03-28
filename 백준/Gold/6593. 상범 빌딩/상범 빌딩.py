import sys
from collections import deque

def bfs(h, x, y) :
    queue = deque()
    queue.append([h, x, y, 0])

    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    while queue :
        h, x, y, distance = queue.popleft()
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]
            if 0 <= nh < L and 0<= nx < R and 0<= ny < C :
                if data[nh][nx][ny] == '.' :
                    queue.append([nh, nx, ny, distance+1])
                    data[nh][nx][ny] = '!'
                elif data[nh][nx][ny] == 'E' :
                    return distance+1
        
while True :
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0 and R == 0 and C == 0 : break
    
    data = []
    for h in range(L) :
        temp = []
        for x in range(R) :
            temp.append(list(map(str, sys.stdin.readline().strip('\n'))))
        data.append(temp)
        input()

    for i in range(L) :
        for j in range(R) :
            for k in range(C) :
                if data[i][j][k] == 'S' :
                    result = bfs(i, j, k)
                    if result == None : print("Trapped!")
                    else : print(f"Escaped in {result} minute(s).")