X, Y = list(map(int, input().split()))

def Reverse(num):
    num0 = num // 100
    num1 = num // 10 - num0*10
    num2 = num % 10
    NEW = num2*100 + num1 * 10 + num0
    return NEW

NEW_X = Reverse(X)
NEW_Y = Reverse(Y)

if(NEW_X > NEW_Y): print(NEW_X)
else:print(NEW_Y)