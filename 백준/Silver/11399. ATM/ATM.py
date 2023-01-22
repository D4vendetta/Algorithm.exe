N = int(input())
data = list(map(int, input().split()))
result = 0

data.sort()
for i in range(N):
    result += data[i]*N
    N -= 1

print(result)