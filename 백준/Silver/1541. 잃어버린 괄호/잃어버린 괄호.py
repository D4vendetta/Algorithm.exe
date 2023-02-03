arr = []
arr = input().split('-')

for j in range(len(arr)):
    result = 0
    for i in arr[j].split('+') :
        result += int(i)
    arr[j] = result

print(arr[0] - sum(arr[1:]))