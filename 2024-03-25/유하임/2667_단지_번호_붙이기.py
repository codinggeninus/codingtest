from collections import deque
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i, j))
print(len(result))
result.sort()
for i in result:
    print(i, sep="\n")