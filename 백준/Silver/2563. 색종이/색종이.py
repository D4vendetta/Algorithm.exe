arr = [[0]*101 for i in range(101)]
result = 0

for _ in range(int(input())):
    A, B= map(int, input().split())
    for m in range(10):
        for n in range(10):
            arr[A+m][B+n] = 1

for b in range(100):
    for c in range(100):
        if arr[b][c] > 0 : result += 1
print(result)