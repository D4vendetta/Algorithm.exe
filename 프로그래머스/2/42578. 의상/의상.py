def solution(clothes):
    dict = {}
    answer = 1
    for i in clothes :
        if i[1] in dict :
            dict[i[1]] += 1
        else : dict[i[1]] = 1
    for j in dict.values() :
        answer *= (j+1)
    return answer-1