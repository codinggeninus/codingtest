def backtracking(N, M, result, start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N + 1):
        backtracking(N, M, result + [i], i)  # 다음에 선택할 수 있는 후보 숫자는 현재 선택한 숫자보다 큰 수로 제한

N, M = map(int, input().split())

backtracking(N, M, [], 1)
