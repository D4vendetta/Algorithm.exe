M, N = map(int, input().split())

A = max(M, N)
B = min(M, N)

for i in range(B, 0, -1):
    if A % i == 0 and B % i == 0:
        print(i)
        break

for j in range(1, 100000):
    if (B * j)% A == 0 :
        print(B*j)
        break