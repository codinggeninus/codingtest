import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    if i <= 2:
        dp[i] = i
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n]%10007)