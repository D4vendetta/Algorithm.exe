result = []

for i in range(1, 10000):
    num_list = list(map(int, str(i)))

    result.append(i + sum(num_list))
    
    if i not in result:
        print(i)