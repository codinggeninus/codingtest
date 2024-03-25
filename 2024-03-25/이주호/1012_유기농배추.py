t = int(input())
result_list = [0 for i in range(t)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >=n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
        return True
    return False

for p in range(t):
    m, n, k = map(int,input().split())
    graph = [[0 for x in range(m)] for y in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result_list[p] += 1

for i in range(t):
    print(result_list[i])
