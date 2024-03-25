import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split()) # 가로, 세로, 상자수
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
d_z = [-1, 1, 0, 0, 0, 0]
d_row = [0, 0, 0, 0, 1, -1]
d_col = [0, 0, -1, 1, 0, 0] 
dq = deque([])
day = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                dq.append([i, j, k])

def bfs():
    while dq:
        z_tmp, row_tmp, col_tmp = dq.popleft()
        for p in range(6):
            z = z_tmp + d_z[p]
            row = row_tmp + d_row[p]
            col = col_tmp + d_col[p]
            if 0 <= z < H and 0 <= row < N and 0 <= col < M and tomato[z][row][col] == 0:
                dq.append([z, row, col])
                tomato[z][row][col] = tomato[z_tmp][row_tmp][col_tmp] + 1

bfs()

for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
            day = max(day, k)

print(day-1)