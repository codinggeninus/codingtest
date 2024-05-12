from collections import deque

def move():
    global jihun, fire, time, visited
    while True:
        time += 1
        
        # 현재 불의 위치를 저장해두기 위한 큐
        new_fire = deque()
        while fire:
            x, y = fire.popleft() # fire 큐에 있는 좌표에 대해
            for i in range(4): # 4방향으로 확산했을 때
                nx, ny = x + dx[i], y + dy[i]
                # 미로 범위 안에 있으면서 불이 아니고 방문한 적이 없는 경우에 F로 바꿔주고 새 좌표 추가
                if 0<=nx<r and 0<=ny<c and maze[nx][ny] != '#' and not visited[nx][ny]:
                    maze[nx][ny] = 'F'
                    visited[nx][ny] = True
                    new_fire.append((nx, ny))
        fire = new_fire  # 불의 위치 업데이트
        # 현재 지훈이의 위치를 저장해두기 위한 큐
        new_jihun = deque()
        while jihun:
            x, y = jihun.popleft() # 지훈이의 좌표
            # 만약 가장자리에 도달했다면 시간을 return
            if x == 0 or x == r-1 or y == 0 or y == c-1:
                return time
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 미로 범위 안에 있으면서 지나갈 수 있는 장소일 때
                if 0<=nx<r and 0<=ny<c and maze[nx][ny] == '.' and not visited[nx][ny]:
                    # 지훈이의 위치를 바꾸고 방문한 곳을 기록
                    maze[x][y] = '#'
                    maze[nx][ny] = 'J'
                    visited[nx][ny] = True
                    new_jihun.append((nx, ny))
        jihun = new_jihun  # 지훈이 위치 업데이트
        if not jihun:
            return False

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]
jihun, fire = deque(), deque()
visited = [[False]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jihun.append((i, j))
            visited[i][j] = True
        elif maze[i][j] == 'F':
            fire.append((i, j))
            visited[i][j] = True
                
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0
if move():
    print(time)
else:
    print("IMPOSSIBLE")
