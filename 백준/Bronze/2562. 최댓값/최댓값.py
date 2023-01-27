data = []
for i in range(9):
    data.append(int(input()))
result, max = 0, 0

for i in range(9) :
    if data[i] > max : 
        max = data[i]
        result = i

print(max)
print(result+1)