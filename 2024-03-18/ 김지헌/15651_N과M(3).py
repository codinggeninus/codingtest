def backtracking(N, M, result):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        backtracking(N, M, result + [i])

N, M = map(int, input().split())

backtracking(N, M, [])
