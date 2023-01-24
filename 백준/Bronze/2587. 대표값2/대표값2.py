data = [0]*5
for i in range(5):
  data[i] = int(input())

data.sort()
mid = data[2]
avg = int(sum(data)/5)

print(avg)
print(mid)