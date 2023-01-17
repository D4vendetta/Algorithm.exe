A, B, C = map(int, input().split())

if(A==B==C) :
    price = 10000+A*1000

elif(A==B or A==C):
    price = 1000+A*100
elif(B==C):
    price = 1000+B*100

else:
    if(A>B):
        if(C>A):price = C*100
        else:price = A*100
    if(B>C):
        if(A>B):price = A*100
        else:price = B*100
    if(C>B):
        if(C>A):price=C*100
        else:price = A*100

print(price)