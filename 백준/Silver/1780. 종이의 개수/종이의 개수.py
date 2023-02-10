import sys

result = []
N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 


def Cutting(x, y, N):
    color = data[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != data[i][j] :
                Cutting(x, y, N//3)
                Cutting(x, y+N//3, N//3)
                Cutting(x, y+(N//3)*2, N//3)
                Cutting(x+N//3, y, N//3)
                Cutting(x+N//3, y+N//3, N//3)
                Cutting(x+N//3, y+(N//3)*2, N//3)
                Cutting(x+(N//3)*2, y, N//3)
                Cutting(x+(N//3)*2, y+N//3, N//3)
                Cutting(x+(N//3)*2, y+(N//3)*2, N//3)
                return
    if color == 0 :
        result.append(0)
    elif color == -1 :
        result.append(-1)
    else :
        result.append(1)

Cutting(0, 0, N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))