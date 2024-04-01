from collections import deque
M, N, H = map(int, input().split())
graph = []
for _ in range(H):
    graph.append([list(map(int, input().split())) for _ in range(N)])


def bfs():
    # 날짜
    count = 0
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k, count))
    while queue:
        z, y, x, count = queue.popleft()
        for dz, dy, dx in [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                queue.append((nz, ny, nx, count + 1))
    return count


result = bfs()
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            exit()
else:
    print(result)