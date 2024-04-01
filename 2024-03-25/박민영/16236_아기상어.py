# 처음 아기상어 크기 2
# 큰 물고기 지나갈 수 없음
# 같은 물고기 지나갈 수만 있음
# 작은 물고기 먹을 수 있음
# 거리가 가까운 물고기가 많다면, 위 -> 왼쪽 순으로
# 아기상어는 자신의 크기와 같은 수의 물고기 먹으면 크기 1 증가

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
shark_size = 2

# 아기상어 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x, y = i, j
            graph[x][y] = 0

# 함수를 반복해서 수행하면서 각 반복마다 잡아먹을 물고기 결정
# 더이상 잡아먹을 물고기 없으면 반복 종료
def fish(x, y, shark_size):
    dq = deque([])
    dq.append([x, y])
    visited = [[0] * N for _ in range(N)] # 방문 여부
    visited[x][y] = 1
    distance = [[0] * N for _ in range(N)] # 아기상어와의 거리
    tmp = [] # 잡아먹은 물고기 위치, 거리
    while dq:
        x_tmp, y_tmp = dq.popleft()
        for i in range(4):
            x_now, y_now = x_tmp + dx[i], y_tmp + dy[i]
            if 0 <= x_now < N and 0 <= y_now < N and not visited[x_now][y_now]:
                # 방문 처리
                if graph[x_now][y_now] <= shark_size:
                    dq.append([x_now, y_now])
                    visited[x_now][y_now] = 1
                    distance[x_now][y_now] = distance[x_tmp][y_tmp] + 1
                # 잡아먹을 수 있는 물고기 
                if 0 < graph[x_now][y_now] < shark_size:
                    tmp.append([x_now, y_now, distance[x_now][y_now]])
    return sorted(tmp, key = lambda x: (-x[2], -x[0], -x[1]))

day = 0 # 이동한 날의 수
cnt = 0 # 잡아먹은 물고기 수
while True:
    res = fish(x, y, shark_size)
    if len(res) == 0: # 잡아먹을 수 있는 물고기가 없을 때
        break
    nx, ny, dist = res.pop()
    cnt += 1 
    day += dist
    x, y = nx, ny
    graph[nx][ny] = 0 # 반드시 먹은 물고기는 0으로 처리
    if cnt == shark_size: # 아기상어 사이즈만큼 물고기 먹었을 때
        shark_size += 1
        cnt = 0

print(day)
