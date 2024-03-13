"""
15652. N과 M (4)
"""
from sys import stdin

input = stdin.readline


def solution1(n, m):
    def dfs(numbers):
        if len(numbers) == m:
            print(" ".join(map(str, numbers)))
            return

        for number in range(1, n + 1):
            if numbers and numbers[-1] > number:
                continue

            numbers.append(number)
            dfs(numbers)
            numbers.pop()

    dfs([])


def solution2(n, m):
    from itertools import combinations_with_replacement
    numbers = [str(i) for i in range(1, n + 1)]
    numbers = map(lambda nums: " ".join(nums), combinations_with_replacement(numbers, m))
    print("\n".join(numbers))


n, m = map(int, input().split())
# solution1(n, m)
solution2(n, m)
