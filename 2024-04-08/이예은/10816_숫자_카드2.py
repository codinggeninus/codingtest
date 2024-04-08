# 이진탐색, 실버5
# https://www.acmicpc.net/problem/10816

import bisect

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()


def binary(list, target):
    left_idx = bisect.bisect_left(list, target)

    if left_idx >= len(list) or list[left_idx] != target:
        return 0
    else:
        right_idx = bisect.bisect_right(list, target)
        return right_idx - left_idx


for i in m_list:
    print(binary(n_list, i), end=" ")
