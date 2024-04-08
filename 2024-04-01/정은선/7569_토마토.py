from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
queue = deque([])
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j))

while queue:
    c, b, a = queue.popleft()
    for i in range(6):
        nx, ny, nz = a + dx[i], b + dy[i], c + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][ny][nx] == 0:
            tomato[nz][ny][nx] = tomato[c][b][a] + 1
            queue.append((nz, ny, nx))

for box in tomato:
    for row in box:
        for t in row:
            if t == 0:
                print(-1)
                exit(0)
        day = max(day, max(t))
print(day - 1)
