M, N = map(int, input().split())
data = []
for i in range(1, M+1):
    if M % i == 0:
        data.append(i)
if len(data) < N:
    print(0)
else : print(data[N-1])