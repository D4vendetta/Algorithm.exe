N = int(input())
arr = []
rank = []

for _ in range(N) :
    A, B= map(int, input().split())
    arr.append((A, B))

for i in range(N):
    count = 0
    for k in range(N):
        if arr[i][0] < arr[k][0] and arr[i][1] < arr[k][1]:
            count += 1
    rank.append(count + 1)

for a in rank:
    print(a, end = " ")