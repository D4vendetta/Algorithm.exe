a = list(input())
b = list(input())

data = []
for i in range(8) :
    data.append(a[i])
    data.append(b[i])

k = 15
while k != 1 :
    for j in range(k) :
        data[j] = (int(data[j])+int(data[j+1]))%10
    data[k] = 0
    k -= 1

print(f"{data[0]}{data[1]}")