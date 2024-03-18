#옛날 풀이
from itertools import product
N, M = map(int, input().split())
com = product(range(1, N+1), repeat=M)
for i in com:
    print(*i)


#오늘 풀이
N, M = map(int, input().split())
result = []
def backtraking():
    if len(result) == M:
        print(*result)
        return #recursion error
    for i in range(1, N+1):
        result.append(i)
        backtraking()
        result.pop()
backtraking()