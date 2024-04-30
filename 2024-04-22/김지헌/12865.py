# 물품의 수 N과 무게 제한 K 입력
N, K = map(int, input().split())

# 각 물건의 무게와 가치 입력
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

# 다이나믹 프로그래밍을 사용하여 최대 가치 계산
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = items[i - 1]
        # 현재 물건을 선택하지 않는 경우
        dp[i][j] = dp[i - 1][j]
        # 현재 물건을 선택하는 경우
        if j >= w:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

# 배낭에 넣을 수 있는 물건들의 가치의 최댓값 출력
print(dp[N][K])
