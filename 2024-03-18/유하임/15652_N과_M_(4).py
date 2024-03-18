#옛날 풀이
from itertools import combinations_with_replacement
N, M = map(int, input().split())
com = combinations_with_replacement(range(1, N+1), M)
for i in com:
    print(*i)


#오늘 풀이
N, M = map(int, input().split())
result = []
def backtraking(start):
    if len(result) == M:
        print(*result)
        return #recursion error
    for i in range(start, N+1):
        result.append(i)
        backtraking(i)
        result.pop()
backtraking(1)