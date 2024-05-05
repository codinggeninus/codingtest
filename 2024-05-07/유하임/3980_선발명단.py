C = int(input())

def backtracking(N, score):
    global result
    if N == 11:
        result = max(result, sum(score))
        return
    for i in range(11):
        if array[N][i] != 0 and not visited[i]:
            visited[i] = True
            backtracking(N + 1, score + [array[N][i]])
            visited[i] = False

for _ in range(C):
    array = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    result = 0
    backtracking(0, [])
    print(result)
