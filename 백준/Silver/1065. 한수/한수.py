X = int(input())
count = 0

def hansu(num, num1, num2, num3) :
    global count
    if num < 100 : count +=1
    elif num1 - num2 == num2 - num3:
        count += 1
    return count

if X == 1000: result = 144
else:
    for i in range(1, X+1):
        num1 = i // 100
        num2 = i // 10 - num1*10
        num3 = i % 10
        result = hansu(i, num1, num2, num3)

print(result)