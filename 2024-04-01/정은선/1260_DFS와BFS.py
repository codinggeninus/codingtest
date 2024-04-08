from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited2 = visited.copy()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()
def dfs(v):
    print(v, end= ' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
def bfs(v):
    visited2[v] = True
    que = deque([v])
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited2[i]:
                que.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)