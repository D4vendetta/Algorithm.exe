import sys

S, K = map(int, sys.stdin.readline().split())
result = 1

if S%K == 0 :
    result = (S//K) ** K
else :
    data = [S//K for _ in range(K)]
    for i in range(S%K):
        data[i] += 1
    for j in range(K):
        result *= data[j]
        
print(result)