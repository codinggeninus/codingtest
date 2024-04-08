### 풀이 1) bfs

import sys
from collections import deque

T = int(sys.stdin.readline())
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

def bfs(i, j):
    dq = deque([[i, j]])
    area[i][j] = 0
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            dx = x + row[k]
            dy = y + col[k]
            if 0 <= dx < N and 0 <= dy < M and area[dx][dy]:
                dq.append([dx, dy])
                area[dx][dy] = 0

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    area = [[0 for _ in range(M)] for _ in range(N)] # 가로 M, 세로 N
    cnt = 0
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        area[y][x] = 1
    for i in range(N):
        for j in range(M):
            if area[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)

### 풀이 2) dfs

import sys

T = int(sys.stdin.readline())
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

def dfs(i, j):
    area[i][j] = 0
    for k in range(4):
        dx = i + row[k]
        dy = j + col[k]
        if 0 <= dx < N and 0 <= dy < M and area[dx][dy]:
            dfs(dx, dy)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    area = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        area[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if area[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
