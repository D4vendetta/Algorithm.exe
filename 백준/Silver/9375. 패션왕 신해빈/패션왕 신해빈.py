import sys
N = int(sys.stdin.readline())

for i in range(N) :
  K = int(sys.stdin.readline())
  data = []
  count = []
  for j in range(K) :
    A, B = map(str, sys.stdin.readline().split())
    if B not in data :
      data.append(B)
      count.append(1)
    else : 
      count[data.index(B)] += 1
  #여기서부터 count
  result = 1
  for m in range(len(data)) :
    result *= (count[m]+1)
  print(result-1)