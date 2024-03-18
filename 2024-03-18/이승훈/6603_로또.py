"""
6603. 로또
"""
from itertools import combinations
from sys import stdin

input = stdin.readline


def solution1():
    while True:
        k, *s = map(int, input().split())

        if k == 0:
            break

        numbers = [" ".join(map(str, combs)) for combs in combinations(s, 6)]
        print("\n".join(numbers), end="\n\n")


def solution2():
    def dfs(nums):
        if len(nums) == 6:
            print(" ".join(map(str, nums)))
            return

        for i in range(0, k):
            if visited[i] or (nums and nums[-1] >= s[i]):
                continue

            visited[i] = True
            nums.append(s[i])
            dfs(nums)
            visited[i] = False
            nums.pop()

    while True:
        k, *s = map(int, input().split())
        visited = [False] * k

        if k == 0:
            break

        dfs([])
        print()


def solution3():
    visited = []

    def dfs(start):
        if len(visited) == 6:
            print(" ".join(map(str, visited)))
            return

        for i in range(start, k):
            if s[i] in visited or (visited and visited[-1] >= s[i]):
                continue

            visited.append(s[i])
            dfs(start + 1)
            visited.remove(s[i])

    while True:
        k, *s = map(int, input().split())

        if k == 0:
            break

        dfs(0)
        print()


# solution1()
# solution2()
solution3()
