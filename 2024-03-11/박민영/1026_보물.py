# 배열 길이 N, 배열 A, B
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]의 최솟값
# 단, B의 수는 재배열 X

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
S = 0

A.sort()

for i in A:
    S += i * max(B)
    B.pop(B.index(max(B)))

print(S)
