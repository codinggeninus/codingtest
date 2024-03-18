# k개의 수, S의 원소 -> 6개의 수를 고르는 경우 출력
# 중복 X, 오름차순 O

import sys
res = []

def back(start):
    if len(res) == 6:
        print(' '.join(map(str, res)))
        return
    for i in range(start, len(lst)):
        res.append(lst[i])
        back(i+1)
        res.pop()

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == 0:
        break
    k = lst.pop(0)
    back(0)
    print()

