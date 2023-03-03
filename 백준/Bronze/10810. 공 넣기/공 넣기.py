import sys
basket = [0] * 101

N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for z in range(i, j+1):
        basket[z] = k

print(*basket[1:N+1])