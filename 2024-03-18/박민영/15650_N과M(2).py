# 1부터 N까지 자연수 중 중복 없이 M개를 고른 수열
# 중복 X, 오름차순 O

import sys

N, M = map(int, sys.stdin.readline().split())
res = []

def back(start):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for i in range(start, N+1):
        res.append(i)
        back(i+1)
        res.pop()

back(1)