# 사람 수 N, 인출 소요 시간 리스트 P
# 인출하는데 필요한 시간의 합의 최솟값 res

import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
res = 0

P.sort()

for i in P:
    res += i * N
    N -= 1

print(res)


