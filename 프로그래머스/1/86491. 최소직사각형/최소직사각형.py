def solution(sizes):
    data = [0, 0]
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1] :
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        data[0] = max(data[0], sizes[i][0])
        data[1] = max(data[1], sizes[i][1])
    answer = data[0] * data[1]
    return answer