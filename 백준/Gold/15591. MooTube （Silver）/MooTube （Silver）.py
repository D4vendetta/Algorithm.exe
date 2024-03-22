from collections import deque
import sys

def bfs(x, usado) :
    visited = [0] * (n+1)
    count = 0
    queue = deque([x])
    visited[x] = 1

    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if i[1] >= usado and visited[i[0]] == 0:
                queue.append(i[0])
                count += 1
            visited[i[0]] = 1
    return(count)

n, q = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

for _ in range(n-1) :
    a, b, usado = map(int, sys.stdin.readline().split())
    graph[a].append((b, usado))
    graph[b].append((a, usado))

for a in range(q) :
    usado, video = map(int, sys.stdin.readline().split())
    print(bfs(video, usado))