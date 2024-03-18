#옛날 풀이
from itertools import combinations
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
com = list(combinations(array, M))
for i in com:
    print(*i)


#오늘 풀이
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result = []
def backtraking(start):
    if len(result) == M:
        print(*result)
    for i in range(start, N):
        if array[i] not in result:
            result.append(array[i])
            backtraking(i+1)
            result.pop()
backtraking(0)