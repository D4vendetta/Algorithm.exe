import sys

a, b = map(int, sys.stdin.readline().split())

list_a = list(map(int, str(a)))
list_b = list(map(int, str(b)))

def change(data, x, y) :
  result = 0
  for i in range(len(data)) : 
    if data[i] == x : data[i] = y
    result = result + data[i] * (10 ** (len(data)-i-1))
  return result

print(change(list_a, 6, 5)+change(list_b, 6, 5), change(list_a, 5, 6)+change(list_b, 5, 6))