import sys
n = int(sys.stdin.readline())

data_input = []
result1, result2 = 0, 0
for _ in range(n):
  data_input.append(list(map(str, sys.stdin.readline().strip())))

#가로 개수 구하기
for x in range(n) :
  stack = 0
  for y in range(n) :
    if data_input[x][y] == '.' :
      stack += 1
    if data_input[x][y] == 'X' :
      if stack >= 2 :
        result1 += 1
      stack = 0
  if stack >= 2 :
    result1 += 1

#세로 개수 구하기
for x in range(n) :
  stack = 0
  for y in range(n) :
    if data_input[y][x] == '.' :
      stack += 1
    if data_input[y][x] == 'X' :
      if stack >= 2 :
        result2 += 1
      stack = 0
  if stack >= 2 :
    result2 += 1

print(result1, result2)