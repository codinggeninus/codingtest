from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):

    # 현재 정점 방문 처리
    visited1[v] = True
    print(v, end=' ')

    # 인접 정점 탐색
    for i in graph[v]:
        # 방문되지 않은 정점이면 dfs 수행
        if visited1[i] == False:
            dfs(i)

def bfs():
    # 큐가 비어있지 않을 때까지 반복
    while queue:
        # 큐에서 정점 꺼내기
        v = queue.popleft()
        visited2[v] = True
        print(v, end=' ')

        # 인접 정점 탐색
        for i in graph[v]:
            # 방문하지 않은 정점이면 큐에 추가
            if visited2[i] == False:
                visited2[i] = True
                queue.append(i)

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
graph[0].append(0)
visited1 = [False for _ in range(n+1)]
visited2 = [False for _ in range(n+1)]
queue = deque([v])

for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)   
    graph[b].append(a)

# 방문한 번호가 작은 정점부터 방문해야 하므로 오름차순 정렬
for i in range(len(graph)):
    graph[i].sort()

dfs(v)
print()
bfs()