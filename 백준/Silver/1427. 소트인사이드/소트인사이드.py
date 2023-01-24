data = list(map(int, input()))

data.sort()
data.reverse()

for i in data:
  print(i, end='')