N = int(input())

def factorial(Num):
    result = 1
    if Num > 0 :
        result = Num * factorial(Num-1)
    return result

print(factorial(N))
