import sys

data = {}
result = []

N, M = map(int, sys.stdin.readline().split())

a = set()
for i in range(N):
	a.add(sys.stdin.readline().strip())

b = set()
for j in range(M):
	b.add(sys.stdin.readline().strip())

result = sorted(list(a&b))

print(len(result))
for k in result :
	print(k)