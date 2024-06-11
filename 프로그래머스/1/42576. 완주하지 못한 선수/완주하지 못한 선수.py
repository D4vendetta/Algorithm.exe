def solution(participant, completion):
    answer = ''
    dict = {}
    for i in participant:
        if i in dict :
            dict[i] += 1
        else : dict[i] = 1
    for j in completion :
        dict[j] -= 1
    
    for k in dict:
        if dict[k] == 1:
            answer = k
            break
            
    return answer