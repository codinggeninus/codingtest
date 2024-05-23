import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for i in range(2, len(dp)):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], 1 + dp[i//3])
    if i % 2 == 0:
        dp[i] = min(dp[i], 1 + dp[i//2])
print(dp[n])