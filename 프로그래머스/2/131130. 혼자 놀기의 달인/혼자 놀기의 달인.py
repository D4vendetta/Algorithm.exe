def solution(cards):
    result = []
    answer = 0
    for i in range(len(cards)):
        if cards[i] == 0 : continue
        temp, cards[i] = cards[i]-1, 0
        point = 1
        while True:
            if cards[temp] == 0 : 
                result.append(point)
                break
            cards[temp], temp = 0, cards[temp]-1
            point += 1
    result.sort()
    if len(result) <= 1 : answer = 0
    else : answer = result[-1]*result[-2]
    return answer