"""
21610. 마법사 상어와 비바라기

- set 대신 2차원 배열을 사용
"""
dx = (0, -1, -1, -1, 0, 1, 1, 1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)

n, m = map(int, input().split())
board = [[int(el) for el in input().split()] for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m)]
clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]


def move(di, steps):
    moved = []

    # 모든 구름이 di 방향으로 si칸 이동한다.
    for x, y in clouds:
        nx, ny = x, y

        for _ in range(steps):
            nx = (nx + dx[di - 1]) % n
            ny = (ny + dy[di - 1]) % n

        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        board[nx][ny] += 1
        removed[nx][ny] = True
        moved.append((nx, ny))

    # 구름이 모두 사라진다.
    clouds.clear()

    # 물복사버그 마법을 시전한다.
    for x, y in moved:
        cnt = 0

        # 대각선 방향을 모두 검사한다. (1, 3, 5, 7)
        for di in range(1, 8, 2):
            nx = x + dx[di]
            ny = y + dy[di]

            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue

            if board[nx][ny] > 0:
                cnt += 1

        board[x][y] += cnt

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    for i in range(n):
        for j in range(n):
            if board[i][j] < 2 or removed[i][j]:
                continue

            board[i][j] -= 2
            clouds.append((i, j))


for command in commands:
    removed = [[False] * n for _ in range(n)]
    move(*command)

print(sum([sum(col) for col in board]))
