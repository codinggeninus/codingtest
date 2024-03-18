# N개의 자연수(리스트 lst) 중에서 M개를 구른 수열
# 중복 X, 오름차순 X

import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
res = []

def back():
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for i in range(0, N):
        if lst[i] not in res:
            res.append(lst[i])
            back()
            res.pop()

back()