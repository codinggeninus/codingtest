import sys
from collections import deque
input = sys.stdin.readline

'''
BFS
'''

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs():
    while queue:
        y, x, time = queue.popleft()

        # 끝까지 도달했을 경우 time 리턴
        if maze[y][x] == 'J' and (x==0 or x==c-1 or y==0 or y==r-1):
            return print(time+1)
        
        # 상, 하, 좌, 우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나는 경우
            if nx < 0 or nx > c-1 or ny < 0 or ny > r-1:
                continue
            # 이동 불가능한 경우
            if maze[ny][nx] != '.' or maze[ny][nx] == 'F' or maze[ny][nx] == '#':
                continue

            if maze[y][x] == 'F':
                maze[ny][nx] = 'F'
                queue.append((ny, nx, time+1))
            elif maze[y][x] == 'J':
                maze[ny][nx] = 'J'
                queue.append((ny, nx, time+1))

    # 미로 끝에 도달하지 못할 경우
    return(print("IMPOSSIBLE"))

r, c = map(int, input().split())
maze = []
queue = deque()
for i in range(r):
    maze.append(list(input().strip()))

# 불을 먼저 큐에 추가
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            queue.append((i, j, 0))

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            queue.append((i, j, 0))
bfs()