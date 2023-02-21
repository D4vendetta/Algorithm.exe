import sys
result = []
A, B = map(int, sys.stdin.readline().split())

def dfs(num, count):
    if num > B : return
    if num == B : result.append(count)
    dfs(num*2, count+1)
    dfs(num*10+1, count+1)

dfs(A, 1)
if result == []: result.append(-1)
print(min(result))