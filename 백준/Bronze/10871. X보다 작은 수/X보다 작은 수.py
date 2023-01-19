N, X= map(int, input().split())
i = 0

num_list = list(map(int, input().split()))

for i in range(0, N):
    if(num_list[i] < X):print(num_list[i], end=" ")