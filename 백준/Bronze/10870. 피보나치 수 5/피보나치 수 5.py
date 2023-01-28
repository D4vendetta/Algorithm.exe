N = int(input())

def Fibonacci(Num):
    if Num <= 1:
        return Num
    return Fibonacci(Num-1) + Fibonacci(Num-2)

print(Fibonacci(N))