import sys
cost, j = 0, -1


n = int(sys.stdin.readline())
distance = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

min_cost = min(price)

for i in range(n-1) :
    if i < j : 
        continue

    if price[i] == min_cost :
        cost += sum(distance[i:]) * price[i]
        break

    elif i == n-2 : 
        cost += price[i]*price[i-1]
        break

    elif price[i] < price[i+1] :
        for j in range(i+1, n) :
            if price[i] > price[j] :
                break
        cost += price[i] * sum(distance[i:j])

    elif price[i] >= price[i+1] :
        cost += price[i]*distance[i]

print(cost)