import sys
DP = [[[0]*(21) for _ in range(21)] for _ in range(21)]

def func(q, w, e):
    if q <= 0 or w <= 0 or e <= 0 : return 1
    if q > 20 or w > 20 or e > 20 : return func(20, 20, 20)
    if DP[q][w][e]: return DP[q][w][e]
    if q < w < e : 
        DP[q][w][e] =  func(q, w, e-1) + func(q, w-1, e-1) - func(q, w-1, e)
        return DP[q][w][e]
    DP[q][w][e] = func(q-1, w, e) + func(q-1, w-1, e) + func(q-1, w, e-1) - func(q-1, w-1, e-1)
    return DP[q][w][e]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1: break
    print(f"w({a}, {b}, {c}) = {func(a, b, c)}")