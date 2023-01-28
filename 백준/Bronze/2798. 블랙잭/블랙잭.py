N, M = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tem = data[i] + data[j] + data[k]
            if tem > M:
                continue
            else :
                result = max(result, tem)

print(result)