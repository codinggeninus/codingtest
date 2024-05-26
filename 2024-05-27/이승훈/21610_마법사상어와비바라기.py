"""
21610. 마법사 상어와 비바라기

- 구름은 (N, 1), (N, 2), (N-1, 1), (N-1, 2) 에서 시작
- 구름 이동은 M번
- i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다.
- 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다.

[시간 복잡도]
M * (N^2*si + N^2*4 + N^2*a)
= 100 * (2500*50 + 2500*4 + 2500*a) = 13,750,000 * a

- 이때 a는 새로운 구름이 기존 그룸에 포함되는지 검사하는 시간
- 이때 a는 python에서 list와 set의 성능 차이로 좌우됨.
    - 참고: [https://wiki.python.org/moin/TimeComplexity]
    - list의 경우 기본 `in` 연산자는 O(n)이 걸림
    - set의 경우 `in` 연산자는 O(1)이 걸림, 이는 내부적으로 set이 해시 테이블로 구현되어 있기 때문!
        - [https://github.com/python/cpython/blob/3.11/Objects/setobject.c]
    - 따라서 list로 비교하면 시간 초과, set으로 비교하면 1초 내로 풀 수 있다.
"""
dx = (0, -1, -1, -1, 0, 1, 1, 1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)

n, m = map(int, input().split())
board = [[int(el) for el in input().split()] for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m)]
clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]


def move(di, steps):
    moved = set()

    # 모든 구름이 di 방향으로 si칸 이동한다.
    for x, y in clouds:
        nx, ny = x, y

        for _ in range(steps):
            nx = (nx + dx[di - 1]) % n
            ny = (ny + dy[di - 1]) % n

        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        board[nx][ny] += 1
        moved.add((nx, ny))

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
            if board[i][j] >= 2 and (i, j) not in moved:
                board[i][j] -= 2
                clouds.append((i, j))


for command in commands:
    move(*command)

print(sum([sum(col) for col in board]))
