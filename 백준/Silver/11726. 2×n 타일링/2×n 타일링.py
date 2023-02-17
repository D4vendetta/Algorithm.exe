def factorial(x):
    n = 1
    for i in range(1,x+1):
        n = n*i 
    return n

N = int(input())
result = 0
for i in range(N//2+1):
    result += factorial(i+N-2*i) // (factorial(i)*factorial(N-2*i))

print(result % 10007)