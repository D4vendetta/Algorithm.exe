import sys

n = int(sys.stdin.readline())
mine = int(sys.stdin.readline())
data = []
result = 0
for i in range(n-1) :
  data.append(int(sys.stdin.readline()))

while True :
  if n == 1 or max(data) < mine : break
  else : 
    data[data.index(max(data))] -= 1
    mine += 1
    result += 1

print(result)