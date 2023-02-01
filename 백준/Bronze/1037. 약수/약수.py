N = int(input())
arr = list(map(int, input().split()))
arr.sort()

if N % 2 == 1 :
    result = arr[N//2] ** 2
else :
    result = arr[N//2-1]*arr[N//2]

print(result)