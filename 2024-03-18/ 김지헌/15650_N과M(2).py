def backtracking(N, M, result, start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N + 1):
        if i not in result:  # 중복되는 수는 선택하지 않음
            backtracking(N, M, result + [i], i + 1)  # 다음 수부터 시작하도록 재귀 호출

N, M = map(int, input().split())

backtracking(N, M, [], 1)
