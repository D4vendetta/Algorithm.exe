N = int(input())
V = int(input())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)
for i in range(V):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(V):
    visited[V] = 1
    for k in graph[V] :
        if visited[k] == 0:
            dfs(k)

dfs(1)
print(sum(visited)-1)