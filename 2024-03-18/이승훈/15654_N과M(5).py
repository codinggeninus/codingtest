"""
15654. N과 M (5)
"""
from sys import stdin

input = stdin.readline


def solution1(n, m):
    visited = [False] * n
    numbers = [int(num) for num in input().split()]
    numbers.sort()

    def dfs(nums):
        if len(nums) == m:
            print(" ".join(map(str, nums)))
            return

        for i in range(n):
            if visited[i]:
                continue

            visited[i] = True
            nums.append(numbers[i])
            dfs(nums)
            visited[i] = False
            nums.pop()

    dfs([])


def solution2(m):
    from itertools import permutations
    numbers = [int(num) for num in input().split()]
    numbers = permutations(map(str, sorted(numbers)), m)
    print('\n'.join(list(map(' '.join, numbers))))


n, m = map(int, input().split())
# solution1(n, m)
solution2(m)
