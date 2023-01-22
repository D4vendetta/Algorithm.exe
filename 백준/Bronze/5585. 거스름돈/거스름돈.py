X = 1000 - int(input())
count = 0

def cal(num):
    global X, count
    A = X // num
    if A > 0 :
        count += A
        X -= A*num
        return count

money_list = [500, 100, 50, 10, 5, 1]

for i in money_list:
    cal(i)
print(count)