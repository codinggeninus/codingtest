#옛날 풀이
from itertools import permutations
N, M = map(int, input().split())
array = list(map(int, input().split()))
com = list(permutations(array, M))
com.sort()
for i in com:
    print(*i)


#오늘 풀이
N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result = []
def backtraking():
    if len(result) == M:
        print(*result)
    for i in array:
        if i not in result:
            result.append(i)
            backtraking()
            result.pop()
backtraking()