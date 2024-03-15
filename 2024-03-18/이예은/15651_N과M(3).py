# 백트래킹, 실버3
# https://www.acmicpc.net/problem/15651
# 1. 백트래킹 중복0
# 2. n^n
# answer[]

n, m = map(int, input().split())
answer = []


def backtracking():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, n+1):
        answer.append(i)
        backtracking()
        answer.pop()


backtracking()
