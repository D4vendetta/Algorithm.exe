N = int(input())
data = [input() for _ in range(N)]
k = -1

data = list(set(data))
N = len(data)
data.sort(key=len)

for i in range(0, N-1):
    if i < k : continue
    if len(str(data[i])) == len(str(data[i+1])):
        for k in range(i, N):
            if len(data[i]) != len(data[k]):
                break
        if k == N-1 : k += 1
        data[i:k] = sorted(data[i:k])

for j in range(N):
    print(data[j])