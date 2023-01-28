N = int(input())
arr = []

for i in range(N):
    A, B= map(int, input().split())
    arr.append((A, B))

arr.sort(key = lambda x:(x[1], x[0]))
for k in range(N):
    print(arr[k][0], arr[k][1])