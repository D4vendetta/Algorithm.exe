import sys

data = list(map(str, sys.stdin.readline().rstrip('\n')))
status = 0
result, temp = [], []

for i in range(len(data)):
    if status == 1:
        result.append(data[i])
        if data[i] == '>' :
            status = 0
        continue
    if data[i] == '<' or data[i] == ' ':
        for j in range(len(temp)):
            result.append(temp[-1-j])
        if data[i] == ' ' :
            result.append(' ')
            temp = []
            continue
        temp = []
        result.append(data[i])
        status = 1
        continue

    temp.append(data[i])
    if i == len(data)-1 :
        for j in range(len(temp)):
            result.append(temp[-1-j])
        temp = []
        
for z in result:
    print(z, end = '')