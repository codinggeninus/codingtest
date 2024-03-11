import sys
N, K = map(int, sys.stdin.readline().strip().split())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))
array.reverse()
result = 0
for i in array:
    if K >= i:
        result += K // i
        K = K % i
print(result)
