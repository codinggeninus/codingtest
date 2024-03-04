"""
2217. 로프

[풀이]
로프의 조합을 ropes라고 하고, 로프의 개수를 l이라고 할 때,
: max_weight = min(ropes) * l (이때, ropes는 정렬되어 있다고 가정)

e.g. ropes = [1, 2, 3, 4]
l=1, max_weight = 4 (4 * 1)
l=2, max_weight = 6 (3 * 2)
l=3, max_weight = 6 (2 * 3)
l=4, ...

e.g. ropes = [60, 20, 700, 47]
l=1, max_weight = 700 (700 * 1)
l=2, max_weight = 120 (60 * 2)
l=3, max_weight = 94 (47 * 2)
l=4, ...
"""
from sys import stdin

input = stdin.readline


def solution(n, k):
    k.sort(reverse=True)
    return max([k[i] * (i + 1) for i in range(n)])


n = int(input())
k = [int(input()) for _ in range(n)]
print(solution(n, k))
