import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = a[:]
for i in range(n):
    for j in range(i+1, n):
        if a[i] < a[j]:
            dp[j] = max(dp[i]+a[j], dp[j])

print(max(dp))
