from collections import deque
import sys
input = sys.stdin.readline

# 토마토가 모두 익을 때까지의 최소 날짜 출력
def bfs():

    while (queue):      
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= ny < n) and (0 <= nx < m) and array[ny][nx] == 0:
                array[ny][nx] += array[y][x] + 1
                queue.append((nx, ny))

m, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            queue.append((j,i))

bfs()
result = 0
for i in range(n):
    if 0 in array[i]:
        print(-1)
        exit(0)
    result = max(result, max(array[i]))

print(result-1)                