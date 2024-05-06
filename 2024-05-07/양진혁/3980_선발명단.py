def perm(player, score):
    global max_score
    if player == 11:
        # print(order, score)
        max_score = max(max_score, score)   # 최대 점수 갱신
        return
    for i in range(11):
        if visited[i] or not stats[player][i]:   # 가지치기. 해당 포지션에서 적합하지 않으면 넘기기 
            continue
        visited[i] = 1      # 방문 가능
        order[player] = i
        perm(player+1, score+stats[player][i])
        order[player] = -1
        visited[i] = 0

# main
t = int(input())
for _ in range(t):
    stats = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    order = [0] * 11
    visited = [0] * 11
    perm(0, 0)
    print(max_score)