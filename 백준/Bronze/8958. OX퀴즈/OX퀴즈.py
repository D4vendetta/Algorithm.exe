N = int(input())

for _ in range(N):
    count, result = 1, 0
    line = list(map(str, input()))
    
    if line[0] == 'O' : result = 1
    for i in range(1, len(line)):
        if line[i] == 'O' :
            if line[i-1] == line[i] :
                count += 1
            result += count
        else : count = 1

    print(result)
    line.clear()