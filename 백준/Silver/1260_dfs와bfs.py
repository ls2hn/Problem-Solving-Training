# https://www.acmicpc.net/problem/1260
from collections import deque
 
n, m, v = map(int, input().split())
 
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
        
for i in range(1, n+1):
    graph[i] = sorted(graph[i])
 
def dfs(v, visited, graph):
    visited[v] = True
    print(v, end=' ')
    for node in graph[v]:
        if not visited[node]:
            dfs(node, visited, graph)
 
def bfs(v, visited, graph):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for item in graph[node]:
            if not visited[item]:
                queue.append(item)
                visited[item] = True
 
visited = [False] * (n+1)
dfs(v, visited, graph)
print()
 
visited = [False] * (n+1)
bfs(v, visited, graph)
