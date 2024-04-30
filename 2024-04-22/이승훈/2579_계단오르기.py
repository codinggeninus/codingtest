"""
2579. 계단 오르기
"""
from sys import stdin

n = int(stdin.readline())


def solution(n):
    nums = [0] * (n + 1)

    for i in range(1, n + 1):
        nums[i] = int(stdin.readline())

    if n == 1:
        return nums[1]

    if n == 2:
        return sum(nums[1:])

    dp = [0] * (n + 1)
    dp[1] = nums[1]
    dp[2] = nums[1] + nums[2]

    for h in range(3, n + 1):
        dp[h] = max(dp[h - 3] + nums[h - 1] + nums[h], nums[h] + dp[h - 2])
    return dp[n]


print(solution(n))
