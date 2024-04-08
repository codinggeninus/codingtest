"""
2805. 나무 자르기
"""
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))


def search(left, right):
    while left < right:
        mid = left + (right - left) // 2
        total = sum([tree - mid for tree in trees if tree > mid])

        if total < m:
            right = mid
        else:
            left = mid + 1
    return left - 1


print(search(0, max(trees)))
