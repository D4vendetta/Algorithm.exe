import sys

S, P = map(int, sys.stdin.readline().split())
data = list(map(str, sys.stdin.readline()))
a, c, g, t = map(int,sys.stdin.readline().split())
result = 0

dna = {'A':0, 'C':0, 'G':0, 'T':0}

start, end = 0, P
temp = data[start:end]

for i in temp:
    if i in dna:
        dna[i] += 1
    else : dna[i] = 1
    
if dna['A'] >= a and dna['C'] >= c and dna['G'] >= g and dna['T'] >= t :
    if dna['A']+dna['C']+dna['G']+dna['T'] == P:
        result += 1

#window 계산 끝

while True:
    dna[data[start]] -= 1
    if end == S : break
    if data[end] in dna:
        dna[data[end]] += 1
    else : dna[data[end]] = 1
    start += 1
    end += 1
    
    if dna['A'] >= a and dna['C'] >= c and dna['G'] >= g and dna['T'] >= t :
        if dna['A']+dna['C']+dna['G']+dna['T'] == P:
            result += 1

print(result)