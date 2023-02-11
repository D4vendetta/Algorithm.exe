import sys

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

if M >= sum(data) : line = max(data)
else :
    line = max(data)
    while True :
        line -= 1
        for i in range(len(data)):
            if data[i] >= line :
                data[i] = line
        if sum(data) <= M : break

print(line)