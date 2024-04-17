import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dp = [[0 for _ in range(2)] for _ in range(n+1)]

    for i in range(n+1):
        if i == 0:
            dp[0][0] = 1
        elif i == 1:
            dp[1][1] = 1
        elif i == 2:
            dp[2][0] = dp[0][0] + dp[1][0]
            dp[2][1] = dp[0][1] + dp[1][1] 
        else:
            dp[i][0] = dp[i-2][0] + dp[i-1][0]
            dp[i][1] = dp[i-2][1] + dp[i-1][1]

    print(dp[n][0], end=' ')
    print(dp[n][1])
