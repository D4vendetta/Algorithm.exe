def solution(nums):
    answer = 0
    dic = []
    for i in nums :
        if i not in dic : dic.append(i)
    if len(dic) <= len(nums)//2 : answer = len(dic)
    else : answer = len(nums)//2
    return answer