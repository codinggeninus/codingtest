# 이미 모두 익어있으면 0 (0이 없음, 1과 -1로만 구성)
# 토마토가 모두 익지 못하는 상황이면 -1 (0이 존재)
# 토마토가 익을 수 있다면 최소 날짜 출력

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split()) # 가로칸, 세로칸
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]
dq = deque([])
day = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            dq.append([i, j])

def bfs():
    while dq:
        row_tmp, col_tmp = dq.popleft()
        for k in range(4):
            row = row_tmp + d_row[k]
            col = col_tmp + d_col[k]
            if 0 <= row < N and 0 <= col < M and tomato[row][col] == 0:
                dq.append([row, col])
                tomato[row][col] = tomato[row_tmp][col_tmp] + 1

bfs()

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        day = max(day, j)

print(day-1)
