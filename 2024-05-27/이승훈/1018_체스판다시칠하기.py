"""
1018. 체스판 다시 칠하기

최악의 경우를 가정해도 총 연산 횟수는:
(n-8)*(m-8)*128 => 42*42*128 = 225,792

따라서 그냥 주먹구구식으로 풀어도 상관 X
"""
n, m = map(int, input().split())
board = [input() for _ in range(n)]
words = 'WB'


def count(x, y):
    """
    2*8*8 = 128
    """
    exchange_count = 1e10

    for k in range(2):
        count = 0
        idx = k

        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if board[i][j] != words[idx]:
                    count += 1
                idx = (idx + 1) % 2
            idx = (idx + 1) % 2

        exchange_count = min(exchange_count, count)
    return exchange_count


answer = 1e10
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        answer = min(answer, count(i, j))

print(answer)
