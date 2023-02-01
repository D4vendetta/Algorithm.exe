while True :
    line = input()
    if line == "." : break
    
    arr = []
    result = "yes"
    for i in line :
        if i == '(':
            arr.append(1)
        elif i == '[':
            arr.append(2)
        elif i == ')':
            if len(arr) == 0 or arr[-1] != 1 : 
                result = "no"
                break
            else : arr.pop()
        elif i == ']':
            if len(arr) == 0 or arr[-1] != 2 : 
                result = "no"
                break
            else : arr.pop()
            
    if len(arr) != 0 : result = "no"
    print(result)