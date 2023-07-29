import sys
a = int(sys.stdin.readline())
data_input = list(map(int, input().split()))
data = sorted(set(data_input))

dic = {}
for i in range(len(data)):
    dic[data[i]] = i

for i in data_input :
    print(dic[i], end = ' ')