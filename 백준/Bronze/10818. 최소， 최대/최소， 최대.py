N = int(input())
num_list = list(map(int, input().split()))
Max = -1000000
Min = 1000000

for i in range(0, N):
    if(num_list[i] > Max) : Max = num_list[i]
    if(num_list[i] < Min) : Min = num_list[i]

print(Min, Max)