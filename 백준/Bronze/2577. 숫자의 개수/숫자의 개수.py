A = int(input())
B = int(input())
C = int(input())

data = [0]*10
for i in str(A*B*C):
    data[int(i)] += 1

for j in data:
    print(j)