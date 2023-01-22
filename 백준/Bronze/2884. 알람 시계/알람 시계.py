A, B= map(int, input().split())
B -= 45
while True:
    if(B<0):
        B += 60
        A -= 1
        continue
    else:break
if(A<0):A+=24

print(A, B)