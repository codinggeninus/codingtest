from collections import deque

N = int(input())
maps = [list(input()) for _ in range(N)]

q = deque()
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
total = 0
cnts = []
count = 0


def DFS(ci, cj):
  if not (0 <= ci < N and 0 <= cj < N):
    return False

  if maps[ci][cj] == '0':
    return False

  global count
  count += 1
  maps[ci][cj] = '0'
  for d in range(4):
    ni, nj = ci + di[d], cj + dj[d]
    DFS(ni, nj)

  return True


for i in range(N):
  for j in range(N):
    if DFS(i, j) == True:
      cnts.append(count)
      total += 1
      count = 0

print(total)
for cnt in sorted(cnts):
  print(cnt)
