# 이진탐색, 실버5
# https://www.acmicpc.net/problem/2776

import bisect

t = int(input())

def binary(list, target):
    idx = bisect.bisect_left(list, target)
    if idx < len(list) and list[idx] == target:
        return 1
    else:
        return 0

for i in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))
    n_list.sort()
    for i in m_list:
        print(binary(n_list, i))
