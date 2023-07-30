import sys

a, b = map(int, sys.stdin.readline().split())
D = [a]

def next_num(N) :
  hap = 0
  number_list = list(map(int, str(N)))
  for i in number_list :
    hap += i ** b
  return hap

while True :
  C = next_num(D[-1])
  if C in D :
    K = D.index(C)
    break
  else : D.append(C)

print(K)