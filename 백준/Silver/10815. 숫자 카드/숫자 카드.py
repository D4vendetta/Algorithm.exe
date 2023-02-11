import sys

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
search = list(map(int,sys.stdin.readline().split()))

data.sort()

def binary(arr, start, end, num):
    pivot = ((end-start)//2)+start
    if arr[pivot] == num:
        return 1
    elif end - start == 1 : return 0
    elif arr[pivot] < num:
        return binary(arr, pivot, end, num)
    else :
        return binary(arr, start, pivot, num)

for i in search :
    print(binary(data, 0, N, i), end = " ")