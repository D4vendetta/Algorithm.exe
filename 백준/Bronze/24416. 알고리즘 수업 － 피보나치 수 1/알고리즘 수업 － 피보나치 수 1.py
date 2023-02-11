n = int(input())
result1, result2 = 0, 0
f = [0]* 50


def fib(n) :
    global result1
    if n == 1 or n == 2 : 
        return 1
    else :
        result1 += 1
        return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    global result2
    if n == 1 or n == 2 : 
        return 1
    if f[n] != 0 : 
        return f[n]
    f[n] = fibonacci(n-1) + fibonacci(n-2)
    result2 += 1
    return f[n]

fib(n)
fibonacci(n)
print(result1+1, result2)