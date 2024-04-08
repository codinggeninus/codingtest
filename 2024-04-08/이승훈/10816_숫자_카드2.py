"""
10816. 숫자 카드 2
"""
from sys import stdin

input = stdin.readline
n = int(input().strip())
cards = list(map(int, input().strip().split()))
m = int(input().strip())
targets = list(map(int, input().strip().split()))

def solution1():
    """내장 함수 사용"""
    from bisect import bisect_left, bisect_right
    return bisect_right(cards, target) - bisect_left(cards, target) 


def solution2(target):
    """직접 구현"""
    def lower_bound(target):
        left, right = 0, n

        while left < right:
            mid = left + (right - left) // 2

            if cards[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound(target):
        left, right = 0, n

        while left < right:
            mid = left + (right - left) // 2

            if cards[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    return upper_bound(target) - lower_bound(target) 


cards.sort()
for target in targets:
    print(solution2(target), end=' ')
