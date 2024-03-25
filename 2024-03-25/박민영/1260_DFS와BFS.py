# 1. 인접 리스트 활용
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [0 for _ in range(N+1)]
visited_bfs = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

def dfs(i):
    visited_dfs[i] = 1
    print(i, end = ' ')
    for j in graph[i]:
        if not visited_dfs[j]:
            dfs(j)

def bfs(i):
    dq = deque([i])
    visited_bfs[i] = 1
    while dq:
        tmp = dq.popleft()
        print(tmp, end = ' ')
        for j in graph[tmp]:
            if not visited_bfs[j]:
                visited_bfs[j] = 1
                dq.append(j)

dfs(V)
print()
bfs(V)

# 2. 인접 행렬 활용
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited_dfs = [0 for _ in range(N+1)]
visited_bfs = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(V):
    visited_dfs[V] = 1 
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] and not visited_dfs[i]:
            dfs(i)

def bfs(V):
    dq = deque([V])
    visited_bfs[V] = 1
    while dq:
        tmp = dq.popleft()
        print(tmp, end = ' ')
        for i in range(1, N+1):
            if graph[tmp][i] and not visited_bfs[i]:
                visited_bfs[i] = 1
                dq.append(i)

dfs(V)
print()
bfs(V)