import sys

N = int(sys.stdin.readline())
result, Num = 0, 1

for i in range(2, N+1):
    Num = Num * i

Num = str(Num)
while Num.endswith('0') == True :
    result += 1
    Num = Num[:-1]

print(result)