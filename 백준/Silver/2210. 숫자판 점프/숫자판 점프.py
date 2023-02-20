import sys
data = []
result = []

def dfs(z, a, line):
    if z <= -1 or z >= 5 or a <= -1 or a>= 5 : return
    if len(line) >= 6: 
        result.append(int(line))
        return
    line = line + str(data[z][a])
    dfs(z+1, a, line)
    dfs(z, a+1, line)
    dfs(z-1, a, line)
    dfs(z, a-1, line)

for _ in range(5):
    data.append(list(map(int, sys.stdin.readline().split())))

for x in range(5):
    for y in range(5):
        dfs(x, y, '')

print(len(set(result)))