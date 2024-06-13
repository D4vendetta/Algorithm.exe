def solution(answers):
    answer = []
    
    data, stack = [], []
    data.append([1, 2, 3, 4, 5])
    data.append([2, 1, 2, 3, 2, 4, 2, 5])
    data.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    for j in range(3):
        temp = 0
        for i in range(len(answers)):
            if data[j][i%len(data[j])] == answers[i] :
                temp += 1
        stack.append(temp)
    for k in range(3):
        if max(stack) == stack[k] : answer.append(k+1)
    return answer