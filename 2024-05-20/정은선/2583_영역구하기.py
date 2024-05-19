from collections import deque

# 빈칸인 경우 해당 영역 사이즈 확인
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    area_size = 0
    while queue:
        cx, cy = queue.popleft()
        area_size += 1
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return area_size

m, n, k = map(int, input().split())
arr = [[False for _ in range(n)] for _ in range(m)]

# 직사각형 색칠 여부 확인
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(n)] for _ in range(m)]
areas = []

# BFS를 통해 각 영역의 크기 계산
for i in range(m):
    for j in range(n):
        if arr[i][j] == False and not visited[i][j]:
            areas.append(bfs(i, j))

# 영역의 개수와 각 영역의 크기 출력
areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))
