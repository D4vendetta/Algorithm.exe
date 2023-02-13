import sys
result = 0

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A.sort(reverse = True)
B.sort()

for i in range(n):
    result += A[i] * B[i]
print(result)