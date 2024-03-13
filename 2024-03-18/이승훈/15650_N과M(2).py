"""
15650. N과 M
"""
from sys import stdin

input = stdin.readline


def solution1(n, m):
    visited = []

    def dfs(start):
        if len(visited) == m:
            print(*visited)
        else:
            for number in range(start, n + 1):
                if number not in visited:
                    visited.append(number)
                    dfs(start + 1)
                    visited.remove(number)

    dfs(1)


def solution2(n, m):
    visited = [False] * (n + 1)

    def dfs(numbers):
        if len(numbers) == m:
            print(*numbers)
            return

        for number in range(1, n + 1):
            if visited[number] or (numbers and numbers[-1] >= number):
                continue

            visited[number] = True
            numbers.append(number)
            dfs(numbers)
            visited[number] = False
            numbers.pop()

    dfs([])


n, m = map(int, input().split())
# solution1(n, m)
solution2(n, m)
