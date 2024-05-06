"""
1106. 호텔

- C <= 1,000
- 1 <= cost, cnt <= 100
- 이때, 주어진 cnt 에 대해 C보다 크거나 같을 때까지 증가시켜야 하므로,
    - C <= cost, cnt <= 99 + C
    - 이때, C는 최대 1,000이므로 1,000 <= cost, cnt <= 1,099

따라서 해당 범위까지 아래 점화식을 적용한다. (dp[k] = 최대 k명까지 늘렸을 때 최소 투자 비용)
    - dp[k] = min(dp[k], dp[k - cnt[i]] + cost[i])

[설명]
- 호텔의 고객 수가 C보다 큰 경우에도 C와 정확히 일치하는 경우보다 비용이 더 적을 수 있다.
    - e.g. C = 10, N = 2
    - (cost, cnt)의 배열 => [(20, 10), (1, 1)]
- 따라서 C명 이상일 때의 최소 비용을 구하기 위해서는 C 이상인 경우의 비용과 비교해 봐야 한다.
- 이때 비교 범위는 1 ~ C+99 까지이며, 즉 사람의 수가 C부터 C+99일때 까지의 비용 중 최소값을 구하면 된다.

[접근 방식]
- 처음 접근할 때는 단순한 구현 문제로 생각
- 그러나 특정 고객 수에 대한 최소 비용을 구하는 과정은 최적 부분 구조를 가짐
- 또한 각 문제가 중복된 부분 문제라는 점에서 다이나믹 프로그래밍으로 접근을 시도
"""
from sys import maxsize

C, N = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(N)]
dp = [maxsize] * 1100  # 0 포함 (1099 + 1)
dp[0] = 0

for i in range(N):
    cost, cnt = costs[i]
    for j in range(cnt, 1100):
        dp[j] = min(dp[j - cnt] + cost, dp[j])

print(min(dp[C:]))
