month = int(input())
date = int(input())

if month > 2 : print("After")
elif month == 2 and date > 18 : print("After")
elif month == 2 and date == 18 : print("Special")
else : print("Before")