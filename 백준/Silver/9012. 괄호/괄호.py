N = int(input())

for _ in range(N):
    count = 0
    result = "YES"
    data = list(map(str, input()))
    for i in data:
        if i == '(':
            count += 1
        else:
            count -= 1

        if count < 0 :
            break
    
    if count != 0 : result = "NO"
    print(result)