import sys

N = int(sys.stdin.readline())
Num, line = N, 1

for i in range(1, 10000000):
    if N > i:
        N -= i
    else : 
        line = i
        break

if line % 2 == 0:
    print(f"{N}/{line + 1 - N}")
else : print(f"{line + 1 - N}/{N}")