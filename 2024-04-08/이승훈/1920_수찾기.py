"""
1920. 수찾기

1. 찾고자 하는 정수 X에 대해 배열 A를 대상으로 이분 탐색을 수행한다.
2. X가 존재한다면 1, 아니라면 0을 출력한다.
3. 이를 N번만큼 반복한다.
"""
from sys import stdin


def bin_search(nums, target):
    start, end = 0, n - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
nums.sort()

for target in targets:
    print(1 if bin_search(nums, target) != -1 else 0)
