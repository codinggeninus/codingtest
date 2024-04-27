import sys
input = sys.stdin.readline

def dfs(depth, s):

    global total
    # 깊이가 11이면 최대값 계산
    if depth == 11:
        total = max(total, s)
        return
    
    for i in range(11):
        if not visited[i] and position[depth][i] != 0:
            visited[i] = 1
            dfs(depth+1, s+position[depth][i])
            visited[i] = 0  

c = int(input())
for _ in range(c):
    position = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    total = 0
    dfs(0, 0)
    print(total)
    