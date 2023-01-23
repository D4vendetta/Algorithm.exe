data = []
for i in range(10):
    data.append(int(input()))

for i in range(10):
    data[i] %= 42

data = set(data)
result = len(data)
print(result)