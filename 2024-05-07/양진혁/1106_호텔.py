c, n = map(int, input().split())
pal = [list(map(int, input().split())) for _ in range(n)]

pal.sort(key= lambda x: (x[0], -x[1]))

print(pal)