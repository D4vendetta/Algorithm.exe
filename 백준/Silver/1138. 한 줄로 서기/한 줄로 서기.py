import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
result = [0]*len(data)

for i in range(len(data)) :
    count = 0
    for j in range(len(result)) :
        if count == data[i] :
            for k in range(j, len(result)) :
                if result[k] == 0 : 
                    result[k] = i+1
                    break
            break
        if result[j] == 0 : count += 1

print(*result)