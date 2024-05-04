"""
1106. 호텔

- C <= 1,000
- 1 <= cost, cnt <= 100
- 이때, 주어진 cnt 에 대해 C보다 크거나 같을 때까지 증가시켜야 하므로,
    - C <= cost, cnt <= 99 + C
    - 이때, C는 최대 1,000이므로 1,000 <= cost, cnt <= 1,099

따라서 해당 범위까지 아래 점화식을 적용한다. (dp[k] = 최대 k명까지 늘렸을 때 최소 투자 비용)
    - dp[k] = min(dp[k], dp[k - cnt[i]] + cost[i])
"""
from sys import maxsize

C, N = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(N)]
dp = [maxsize] * 1100  # 0 포함 (1099 + 1)
dp[0] = 0

for i in range(N):
    cost, cnt = costs[i]
    for j in range(cnt, 1100):
        dp[j] = min(dp[j-cnt] + cost, dp[j])

print(min(dp[C:]))
