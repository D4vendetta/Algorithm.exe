N = int(input())

for j in range(1, N+1):
    count = 0
    for i in str(j):
        count += int(i)
    if count+j == N : 
        print(j)
        break
    if j == N : print("0")