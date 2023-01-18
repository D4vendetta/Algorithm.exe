N = int(input())
sum = 0
Max = 1

num_list = list(map(int, input().split()))

for i in range(0, N):
    if(num_list[i] > Max) : Max = num_list[i]

for i in range(0, N):
    num_list[i] = num_list[i]/Max*100

for i in range(0, N) :
    sum += num_list[i]

avg = sum / N
print(avg)