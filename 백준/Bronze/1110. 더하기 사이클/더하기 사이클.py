N= int(input())
X = N//10
Y = N%10
i = 0

while True:
    sum = X + Y
    New = Y*10+(sum%10)
    i += 1
    if(New == N) : 
        break
    else:
        X = New//10
        Y = New%10
        continue
print(i)