import sys

A, B = map(int, input().split())
dic = {}
for j in range(A) :
    site, password = map(str, sys.stdin.readline().split())
    dic[site] = password

for k in range(B) :
    qustion = str(sys.stdin.readline().rstrip('\n'))
    print(dic[qustion])