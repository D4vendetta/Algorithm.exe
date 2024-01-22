import sys

N, M = map(int, sys.stdin.readline().split())
data = []
for i in range(M) :
    data.append(int(sys.stdin.readline()))

data.sort()
result, final_price, total = 0, 0, 0
for j in range(M) :
    price = data[j]
    if len(data[j:]) >= N :
        total = N*price
    else : total = len(data[j:])*price

    if result < total :
        final_price = price
        result = total
        

print(final_price, result)
