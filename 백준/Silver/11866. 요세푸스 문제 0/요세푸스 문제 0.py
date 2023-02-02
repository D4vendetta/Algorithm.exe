from collections import deque
queue = deque()
arr = []

N, K = map(int, input().split())
for i in range(1, N+1) :
    queue.append(i)

while True:
    if len(queue) == 0 : break
    for _ in range(K-1):
        queue.append(queue.popleft())
    arr.append(queue.popleft())

print("<", end = "")
for z in arr :
    if z == arr[-1] : print(f"{z}>", end = "")
    else : print(f"{z}, ", end = "")