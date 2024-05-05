N = int(input())
array = list(map(int, input().split()))
d = [0] * (N + 1)
d[0] = array[0]
for i in range(N):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + array[i])
        # elif d[i] == 0:
        #     d[i] = array[i]
print(max(d))