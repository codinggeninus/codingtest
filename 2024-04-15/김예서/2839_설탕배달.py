import sys
input = sys.stdin.readline

n = int(input())
dp = [-1] * (n+1)

# 3킬로그램 봉지와 5킬로그램 봉지로 N킬로 그램 봉지를 만들기 위한 최소 개수 구하기

dp[3] = 1
if n >= 5:
    dp[5] = 1 

for i in range(4, n+1):
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    elif dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
    
print(dp[n])