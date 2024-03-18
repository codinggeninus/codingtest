# 옛날 풀이
from itertools import combinations
N, M = map(int, input().split())
com = list(combinations(range(1, N+1), M))
for i in com:
    print(*i)

#오늘 풀이
N, M = map(int, input().split())
result = []
def backtraking(start):
    if len(result) == M:
        print(*result)
    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            backtraking(i+1)
            result.pop()
backtraking(1)