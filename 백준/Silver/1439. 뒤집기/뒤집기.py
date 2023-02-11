import sys

arr = (list(map(int, input())))

def Count(arr, num, verse):
    arr_2 = arr[:]
    count = 0
    while True :
        if arr_2.count(num) == 0 : 
            return count
        for i in range(0, len(arr_2)):
            if arr_2[i] == num:
                count += 1
                for j in range(i, len(arr_2)):
                    if  arr_2[j] != num:
                        break
                    else : 
                        arr_2[j] = verse

print(min(Count(arr, 0, 1), Count(arr, 1, 0)))