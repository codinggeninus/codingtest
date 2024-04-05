"""
2776. 암기왕

1. 수찾기(1920) 응용 문제
2. 주어진 테스트 케이스(T) 만큼 다음을 수행
    1. 찾고자 하는 정수 X에 대해 배열 A를 대상으로 이분 탐색을 수행한다.
    2. X가 존재한다면 1, 아니라면 0을 출력한다.
    3. 이를 N번만큼 반복한다
"""
from bisect import bisect_left
from sys import stdin


def exists(nums, target):
    def sol1(nums, target):
        """
        수행 시간: 5068ms
        """
        start, end = 0, n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def sol2(nums, target):
        """
        수행 시간: 2644ms
        """
        return (idx := bisect_left(nums, target)) != n and nums[idx] == target

    return sol2(nums, target)


input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))
    nums.sort()
    print('\n'.join(['1' if exists(nums, target) else '0' for target in targets]))
