N = int(input())
arr = [[]for i in range(N)]
age = [0]*N

for i in range(N):
    A, B = map(str, input().split())
    arr[i].append(A)
    arr[i].append(B)
    age[i] = int(A)
age = list(set(age))
age.sort()
j = len(age)

for i in range(j) :
    for k in range(N):
        if age[i] == int(arr[k][0]):
            print(arr[k][0], arr[k][1])