A, B= map(int, input().split())
C = int(input())

B += C
while True:
    if(B>59):
        B -= 60
        A += 1
        continue
    else:break
if(A>23):A-=24

print(A, B)