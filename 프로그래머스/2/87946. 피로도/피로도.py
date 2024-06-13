from itertools import permutations

def solution(k, dungeons):
    answer = 0
    data = list(permutations(dungeons))
    for i in data:
        stack, status = 0, k
        for j in i:
            if status < j[0] : break
            status -= j[1]
            stack += 1
        answer = max(answer, stack)
    return answer