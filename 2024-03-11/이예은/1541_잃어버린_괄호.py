# 그리디, 실버2
# https://www.acmicpc.net/problem/1541

n = input().split('-')

result = []

for i in n:
    s = 0
    temp = i.split('+')
    for j in temp:
        s += int(j)
    result.append(s)

first = result[0]
rest = sum(result[1:])

print(first - rest)