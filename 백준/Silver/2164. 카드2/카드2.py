from collections import deque

queue = deque()
for i in range(int(input())):
    queue.append(i+1)

while True :
    if len(queue) == 1 : 
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())