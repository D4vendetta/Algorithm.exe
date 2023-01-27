N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
arr3 =  [0] * M

for i in range(N):
    for j in range(M):
        arr3[j] = arr1[i][j] + arr2[i][j]
    print(*arr3)