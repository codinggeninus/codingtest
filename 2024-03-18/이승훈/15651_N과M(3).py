"""
15651. N과 M (3)
"""
from sys import stdin

input = stdin.readline


def solution1(n, m):
    def dfs(numbers):
        if len(numbers) == m:
            print(*numbers)
            return

        for number in range(1, n + 1):
            numbers.append(number)
            dfs(numbers)
            numbers.pop()

    dfs([])


def solution2(n, m):
    from itertools import product
    numbers = [str(i) for i in range(1, n + 1)]
    numbers = map(lambda nums: " ".join(nums), product(numbers, repeat=m))
    print("\n".join(numbers))


n, m = map(int, input().split())
# solution1(n, m)
solution2(n, m)
