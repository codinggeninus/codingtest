# 이진탐색, 실버5
# https://www.acmicpc.net/problem/1920

import bisect

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
# 기준이 되는 리스트만 정렬
n_list.sort()


def binary(list, target):
    idx = bisect.bisect_left(list, target)

    if idx < len(list) and list[idx] == target:
        return 1
    else:
        return 0


for i in m_list:
    print(binary(n_list, i))
