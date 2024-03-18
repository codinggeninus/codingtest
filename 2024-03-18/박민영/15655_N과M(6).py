# N개의 자연수(리스트 lst)에서 M개를 고른 수열
# 중복 X, 오름차순 O

import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
res = []

def back(start):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for i in range(start, N):
        res.append(lst[i])
        back(i+1)
        res.pop()

back(0)