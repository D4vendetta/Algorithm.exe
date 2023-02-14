import sys
result, stack = 0, 0

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
for i in data:
    if i == 1 : continue
    if i == 2 : result += 1
    for j in range(2, i):
        if i % j == 0: 
            stack = 0
            break
        else : stack = 1
    result += stack

print(result)