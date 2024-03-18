# 1부터 N까지 자연수 중 M개를 고른 수열
# 중복 O, 오름차순 X

import sys

N, M = map(int, sys.stdin.readline().split())
res = []

def back():
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for i in range(1, N+1):
        res.append(i)
        back()
        res.pop()

back()