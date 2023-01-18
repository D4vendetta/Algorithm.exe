X = int(input())
N = int(input())
sum = 0

for i in range(1, N+1) :
    A, B= map(int, input().split())
    sum += A * B

if(X == sum):print("Yes")
else:print("No")