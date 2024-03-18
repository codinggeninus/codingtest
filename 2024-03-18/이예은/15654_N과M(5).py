# 백트래킹, 실버3
# https://www.acmicpc.net/problem/15654
# 1. 백트래킹, n개의 수가 주어짐, 중복x, 
# 2. n^n <= 8
# 3. answer[]

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
answer = []


def backtracking(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(n):
        if n_list[i] not in answer:
            answer.append(n_list[i])
            backtracking(start+1)
            answer.pop()


backtracking(0)
