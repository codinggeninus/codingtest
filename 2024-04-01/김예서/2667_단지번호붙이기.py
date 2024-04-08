import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs(x, y):

    global cnt

    if visited[y][x] == -1:
        cnt += 1
        visited[y][x] = cnt

    # 상, 하, 좌, 우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 넘어서는 경우 continue
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
            continue
        
        # 이미 방문한 경우 continue
        if visited[ny][nx] != -1:
            continue

        # 1인 경우 dfs 수행
        if graph[ny][nx] == 1:
            dfs(nx, ny)

n = int(input())
graph = []
visited = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().strip()))
    graph.append(a)

result = []
for i in range(n):
    for j in range(n):
        # 존재하는 집이라면
        if graph[i][j] == 1 and visited[i][j] == -1:
            cnt = 0
            dfs(j, i)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)