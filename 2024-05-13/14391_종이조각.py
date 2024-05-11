"""
14391. 종이 조각
"""
N, M = map(int, input().split())
board = [[int(el) for el in input()] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0


def dfs(r, c):
    global answer

    if r == N:
        total = 0

        for i in range(N):
            col_sum = 0
            for j in range(M):
                if visited[i][j]:
                    col_sum = col_sum * 10 + board[i][j]
                else:
                    total += col_sum
                    col_sum = 0
            total += col_sum

        for i in range(M):
            row_sum = 0
            for j in range(N):
                if not visited[j][i]:
                    row_sum = row_sum * 10 + board[i][j]
                else:
                    total += row_sum
                    row_sum = 0
            total += row_sum

        answer = max(total, answer)
        return

    if c == M:
        dfs(r + 1, 0)
        return

    visited[r][c] = True
    dfs(r, c + 1)

    visited[r][c] = False
    dfs(r, c + 1)


dfs(0, 0)
print(answer)
