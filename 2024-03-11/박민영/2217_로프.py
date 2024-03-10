# N개의 로프, 각 로프의 최대 중량
# 로프 이용해 들 수 있는 최대 중량

# ex) 10 15 20
# 로프 1개 -> 20
# 로프 2개 -> 15 * 2
# 로프 3개 -> 10 * 3

import sys

N = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(N)]
rope.sort()
res = 0

for i in rope:
    tmp = i * N
    if tmp > res:
        res = tmp
    N -= 1

print(res)
