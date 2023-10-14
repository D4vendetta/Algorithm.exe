import sys

N, M = map(int, sys.stdin.readline().split())

dogam = {}

for i in range(N) :
    dogam[i+1] = sys.stdin.readline().strip()

reverse_dogam = {v:k for k,v in dogam.items()}

for j in range(M) :
    qustion = sys.stdin.readline().strip()
    if qustion.isdigit() :
        print(dogam[int(qustion)])
    else :
        print(reverse_dogam[qustion])