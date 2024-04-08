# https://develop247.tistory.com/361

N, M = map(int, input().split())
hgt = list(map(int, input().split()))
hgt.sort()
s, e = 1, max(hgt)
result = 0

def tree(num):
    res = 0
    for i in hgt:
        if i >= num:
            res += (i-num)
    return res

while s <= e:
    mid = (s + e) // 2
    res = tree(mid)
    if res >= M:
        result = mid
        s = mid + 1
    elif res < M:
        e = mid - 1

print(result)


