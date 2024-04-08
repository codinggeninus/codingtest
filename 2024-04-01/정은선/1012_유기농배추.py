import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a, b):
    if a < 0 or a >= n or b < 0 or b >= m or graph[a][b] != 1:
        return
    graph[a][b] = 0
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        dfs(x, y)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    worm = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                worm += 1

    print(worm)
