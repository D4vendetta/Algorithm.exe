mush = []
sum, result_A, result_B = 0, 0, 0

for _ in range(10):
    mush.append(int(input()))

for i in range(10):
    result_A = sum
    sum += mush[i]
    if sum > 100 : 
        result_B = sum
        break
if(result_B == 0) : print(sum)
elif (100 - result_A) == (result_B - 100) : print(result_B)
elif(100 - result_A) > (result_B - 100) : print(result_B)
else : print(result_A)