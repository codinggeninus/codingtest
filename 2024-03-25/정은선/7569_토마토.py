from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
day = 1
tomato = []
queue = deque([])

for k in range(h):
    box = []
    for i in range(n):
        row = list(map(int, input().split()))
        box.append(row)
        for j in range(m):
            if row[j] == 1:
                queue.append((i, j, k))
    tomato.append(box)

while queue:
    a, b, c = queue.popleft()
    for i in range(6):
        nx, ny, nz = a + dx[i], b + dy[i], c + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][ny][nx] == 0:
            tomato[nx][ny][nz] = tomato[a][b][c] + 1
            queue.append((nx, ny, nz))

for box in tomato:
    for row in box:
        for t in row:
            if t == 0:
                print(-1)
                exit(0)
        day = max(day, max(t))
print(day - 1)
