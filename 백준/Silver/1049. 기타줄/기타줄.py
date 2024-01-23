import sys
import math

n, m = map(int, sys.stdin.readline().split())
minor_a, minor_b = 1000, 1000

for i in range(m) :
  a, b = map(int, sys.stdin.readline().split())
  if a < minor_a : minor_a = a
  if b < minor_b : minor_b = b

print(min((n//6)*minor_a+(n%6)*minor_b, n*minor_b, math.ceil(n/6)*minor_a))