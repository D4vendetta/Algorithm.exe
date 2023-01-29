N = int(input())
data = list(map(int, input().split()))
V = int(input())
count = 0

for i in data:
    if V == i : count += 1

print(count)