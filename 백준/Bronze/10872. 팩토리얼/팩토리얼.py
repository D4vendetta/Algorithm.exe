N = int(input())
result = 1

def factorial(Num):
    global result
    if Num <= 1: return result
    result *= Num
    Num -= 1
    factorial(Num)

factorial(N)
print(result)