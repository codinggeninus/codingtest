from collections import deque

def dfs(start):
    global visited
    print(start, end=" ")
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)

def bfs(start):
    global visited
    visited[start] = True
    q = deque([start])

    while q:
        current = q.popleft()
        print(current, end=" ")
        for node in graph[current]:
            if not visited[node]:
                q.append(node)
                visited[node] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False for _ in range(N+1)]
dfs(V)

print()

visited = [False for _ in range(N+1)]
bfs(V)
