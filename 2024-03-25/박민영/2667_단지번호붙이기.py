### 풀이 1) bfs
import sys
from collections import deque

N = int(sys.stdin.readline())
danji = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
row = [-1, 0, 1, 0] # 행 방향 인덱스
col = [0, 1, 0, -1] # 열 방향 인덱스
res = [] # 총 단지수 저장할 리스트

# 총 단지수 카운트하는 함수
def bfs(i, j):
    dq = deque([[i, j]])
    danji[i][j] = 0
    cnt = 1
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            dx = x + row[k]
            dy = y + col[k]
            if 0 <= dx < N and 0 <= dy < N and danji[dx][dy]:
                dq.append([dx, dy])
                danji[dx][dy] = 0
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if danji[i][j]:
            cnt = bfs(i, j)
            res.append(cnt)

res.sort()
print(len(res))
for i in res:
    print(i)


### 풀이 2) dfs
import sys

N = int(sys.stdin.readline())
danji = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
res = []
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

def dfs(i, j):
    global cnt
    danji[i][j] = 0
    cnt += 1
    for k in range(4):
        dx = i + row[k]
        dy = j + col[k]
        if 0 <= dx < N and 0 <= dy < N and danji[dx][dy]:
            dfs(dx, dy)
    return cnt

for i in range(N):
    for j in range(N):
        if danji[i][j]:
            cnt = 0
            cnt = dfs(i, j)
            res.append(cnt)

res.sort()
print(len(res))
for i in res:
    print(i)