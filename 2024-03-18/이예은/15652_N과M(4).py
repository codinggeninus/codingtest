# 백트래킹, 실버3
# https://www.acmicpc.net/problem/15652
# 1. 백트래킹 중복0, 오름차순
# 2. N^M
# answer[]

n, m = map(int, input().split())
answer = []


def backtracking(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, n+1):
        answer.append(i)
        backtracking(i)
        answer.pop()


backtracking(1)
