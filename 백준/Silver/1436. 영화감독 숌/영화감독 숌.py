N = int(input())
data = []
count = 0

for i in range(100000000):
    if "666" in str(i):
        data.append(i)
        count += 1
    if count == N:
        print(data[-1])
        break