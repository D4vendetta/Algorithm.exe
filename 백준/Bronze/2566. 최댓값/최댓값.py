arr = [list(map(int, input().split())) for _ in range(9)]
max = -1
x, y = 0, 0

for i in range(9):
    for j in range(9):
        if max < arr[i][j] :
            max = arr[i][j]
            x = i+1
            y = j+1

print(max)
print(x, y)