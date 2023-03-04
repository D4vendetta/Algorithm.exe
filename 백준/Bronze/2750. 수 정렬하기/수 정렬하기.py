N = int(input())
data = []

for _ in range(N):
    data.append(int(input()))

data.sort()
for k in data:
    print(k)