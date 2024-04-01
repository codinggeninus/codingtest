n = int(input())
graph = []
group = []
count = 0
for _ in range(n):
    row = input()
    graph.append([int(x) for x in row])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a, b):
    global count
    count += 1
    graph[a][b] = 0
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < n and graph[x][y] == 1:
            dfs(x, y)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            group.append(count)
            count = 0

group.sort()
print(len(group))
for i in group:
    print(i)