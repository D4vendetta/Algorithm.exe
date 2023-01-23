N = int(input())
ary = []
ary.append(1)
result = 0

for i in range(0, 100000):
    ary.append(ary[i] + (6*(i+1)))
    if ary[i] >= N :
        result = i+1
        break

print(result)