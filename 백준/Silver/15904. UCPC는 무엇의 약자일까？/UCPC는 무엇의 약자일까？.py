import sys
result = ''
index, index2, index3, index4 = 0, 0, 0, 0

line = sys.stdin.readline()
for i in line :
    if i.isupper() == True:
        result = result + i

index = result.find('U')
index2 = index + result[index:].find('C')
index3 = index2 + result[index2:].find('P')
index4 = index3 + result[index3:].find('C')

if index < index2 and index2 < index3 and index3 < index4 : print("I love UCPC")
else : print("I hate UCPC")