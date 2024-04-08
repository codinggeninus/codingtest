import sys

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
s, e = 1, max(lan) # 최소 길이, 최대 길이
res = 0

while s <= e:
    m = (s + e) // 2
    cnt = 0
    for i in lan:
        cnt += i // m
    if cnt < N:
        e = m - 1
    else:
        res = m
        s = m + 1

print(res)
