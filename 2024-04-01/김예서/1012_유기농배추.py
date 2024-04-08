import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs():
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue

            graph[ny][nx] = 0
            queue.append((nx, ny))
    
t = int(input())
for _ in range(t):
    # 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    
    # 배추의 위치 저장
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((j, i))
                bfs()   
                cnt += 1 
    print(cnt)