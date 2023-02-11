import sys

E1, S1, M1 = map(int, sys.stdin.readline().split())
E, S, M, count= 1, 1, 1, 1

while True :
    if E == E1 and S == S1 and M == M1 :
        print(count)
        break

    E += 1
    S += 1
    M += 1
    if E == 16 : E = 1
    if S == 29 : S = 1
    if M == 20 : M = 1
    count += 1