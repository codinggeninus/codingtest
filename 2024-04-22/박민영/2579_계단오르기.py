N = int(input())
st = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = st[i]
    elif i == 2:
        dp[i] = st[i-1] + st[i]
    else:
        # 1. 바로 이전 계단을 밟는 경우 (전전전 + 전 + 현재)
        # 2. 바로 이전 계단을 밟지 않는 경우 (전전 + 현재)
        dp[i] = max(dp[i-3] + st[i-1] + st[i], dp[i-2] + st[i])

print(dp[N])