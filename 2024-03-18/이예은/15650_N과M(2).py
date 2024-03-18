# 백트래킹, 실버3
# https://www.acmicpc.net/problem/
# 1. n, m을 for 문을 돌면서 재귀 실행 (백트래킹) 중복x
# 2. n! < 8
# 3. answer[]
n, m = map(int, input().split())
answer = []


def dfs(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n+1):
        if i not in answer:
            answer.append(i)
            dfs(i+1)
            answer.pop()


dfs(1)
