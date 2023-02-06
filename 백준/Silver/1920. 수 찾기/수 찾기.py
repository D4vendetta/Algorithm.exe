N = int(input())
arr_A = list(map(int, input().split()))
M = int(input())
arr_X = list(map(int, input().split()))

arr_A.sort()

def Search(arr, X, start, end) :
    if start > end : return 0

    mid = (start + end) // 2
    if arr[mid] == X :
        return 1
    elif arr[mid] > X :
        return Search(arr, X, start, mid-1)
    elif arr[mid] < X :
        return Search(arr, X, mid+1, end)

end = len(arr_A)-1
for i in range(len(arr_X)) :
    print(Search(arr_A, arr_X[i], 0, end))