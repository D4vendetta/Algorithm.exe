import sys

N, M = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
sumsum = [0]
mysum = 0

for i in range(N):
    mysum += data[i]
    sumsum.append(mysum)

for j in range(M) :
    A, B =  map(int,sys.stdin.readline().split())
    print(sumsum[B] - sumsum[A-1])