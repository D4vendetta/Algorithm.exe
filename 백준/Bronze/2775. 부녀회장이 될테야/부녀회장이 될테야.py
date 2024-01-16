import sys

dp = [[0 for _ in range(14)] for _ in range(100)]
for z in range(14) :
    dp[0][z] = z+1

def dp_algo(floor, ho) :
    while dp[floor][ho-1] == 0 :
        for j in range(1, floor+1) :
            for k in range(0, ho) :
                if k == 0 : dp[j][0] = dp[j-1][0]
                else : dp[j][k] = dp[j][k-1] + dp[j-1][k]

n = int(sys.stdin.readline())
for i in range(n) :
    floor = int(sys.stdin.readline())
    ho = int(sys.stdin.readline())

    dp_algo(floor, ho)
    print(dp[floor][ho-1])