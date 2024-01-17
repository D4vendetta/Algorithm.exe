import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
if a == 0 :
    y = c/b
    x = (f - e*y) / d
elif b == 0 :
    x = c/a
    y = (f - d*x) / e
elif d == 0 :
    y = f/e
    x = (c - b*y) / a
elif e == 0 :
    x = f/d
    y = (c - a*x) / b
else : 
    x = (b*f - e*c) / (b*d - a*e)
    y = (c - a*x) / b

print(int(x), int(y))