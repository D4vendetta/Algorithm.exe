import sys
cost = 0


n = int(sys.stdin.readline())
distance = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

min_cost = min(price)
better_cost = 0
j = -1

for i in range(n-1) :
    if i <= j : 
        continue
    if price[i] == min_cost :
        cost += sum(distance[i:]) * price[i]
        break

    elif price[i] < price[i+1] :
        for j in range(i+1, n-1) :
            if price[i] > price[j] :
                break
        cost += price[i] * sum(distance[i:j+1])

    elif price[i] >= price[i+1] :
        cost += price[i]*distance[i]

print(cost)