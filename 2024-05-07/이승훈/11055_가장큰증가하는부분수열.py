"""
11055. 가장 큰 증가하는 부분 수열
"""
from sys import stdin

input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = A[::]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
