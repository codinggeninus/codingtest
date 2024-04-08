import sys
input = sys.stdin.readline
from collections import deque

# 연산자 정의: 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [-1, 1, 0, 0, 0, 0]
def bfs():

    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            if graph[nz][ny][nx] == -1:
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))

# 가로, 세로, 높이
m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                queue.append((k, i, j))

bfs()

cnt = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
            cnt = max(cnt, graph[k][i][j])

print(cnt-1)