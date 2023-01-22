N, K= map(int, input().split())
coin_list = []
for i in range(N):
    coin_list.append(int(input()))
result = 0

for i in range(1, N+1):
    A = K // coin_list[N-i]
    if A >= 1 :
        result += A
        K %= coin_list[N-i]

print(result)