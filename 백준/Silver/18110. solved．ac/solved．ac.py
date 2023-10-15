import sys
data = []

def round45(num) :
    return int(num) + [0, 1][num - int(num) >= 0.5]

N = int(sys.stdin.readline())
for _ in range(N) :
    data.append(int(sys.stdin.readline()))

data.sort()

if N == 0 : print(0)
else : 
    A = round45(N*0.15)
    avg = data[A : len(data)-A]
    print(round45(sum(avg) / len(avg)))