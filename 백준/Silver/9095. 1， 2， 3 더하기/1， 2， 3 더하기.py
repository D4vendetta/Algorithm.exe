import sys
N = int(sys.stdin.readline())
DP = [1, 2, 4]

for j in range(3, 11):
    DP.append(DP[j-3] +  DP[j-2] + DP[j-1])

for _ in range(N) :
    Num = int(sys.stdin.readline())
    print(DP[Num-1])