def dfs(graph, x, y):
    # 방문한 위치를 표시
    visited[x][y] = True
    # 상, 하, 좌, 우 방향으로 이동하며 연결된 배추 위치를 탐색
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        # 배추 밭을 벗어나지 않고, 아직 방문하지 않은 배추가 있는 경우
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] and not visited[nx][ny]:
            dfs(graph, nx, ny)

# 테스트 케이스의 개수 입력
T = int(input())

for _ in range(T):
    # 가로길이 M, 세로길이 N, 배추의 위치 개수 K 입력
    M, N, K = map(int, input().split())
    # 배추 밭 초기화
    field = [[0] * M for _ in range(N)]
    # 방문 여부 초기화
    visited = [[False] * M for _ in range(N)]
    # 배추 위치 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1  # 배추 위치를 1로 표시 (배추가 있는 곳)
    # 필요한 배추흰지렁이의 개수 초기화
    count = 0
    # 모든 위치에 대해 탐색
    for i in range(N):
        for j in range(M):
            # 배추가 있는 위치이고, 아직 방문하지 않은 경우
            if field[i][j] and not visited[i][j]:
                dfs(field, i, j)  # DFS 탐색
                count += 1  # 연결된 배추 그룹을 한 그룹으로 카운트
    print(count)  # 필요한 배추흰지렁이의 개수 출력
