def solution(brown, yellow):
    for a in range(1, brown) :
        b = (brown + yellow) // a
        if (a-2)*(b-2) == yellow and a*b - yellow == brown :
            answer = [max(a, b), min(a, b)]
            break
    return answer