def backtracking(S, k, result, idx):
    if len(result) == 6:
        print(' '.join(map(str, result)))
        return
    
    for i in range(idx, k):
        backtracking(S, k, result + [S[i]], i + 1)

while True:
    data = list(map(int, input().split()))
    k = data[0]
    if k == 0:
        break
    S = data[1:]
    
    backtracking(S, k, [], 0)
    print()
