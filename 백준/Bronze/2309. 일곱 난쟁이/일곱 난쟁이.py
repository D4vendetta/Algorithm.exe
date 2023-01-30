arr = []

for i in range(9):
    arr.append(int(input()))

num = sum(arr) - 100

for j in range(9):
    for k in range(j+1, 9):
        if arr[j] + arr[k] == num:
            A, B = arr[j], arr[k]
            break

arr.remove(A)
arr.remove(B)
arr.sort()

for z in arr:
    print(z)