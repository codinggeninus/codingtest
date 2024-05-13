k = int(input())
arr = []
for _ in range(k):
    n = int(input())
    if n == 0:
        arr.pop(-1)
    else:
        arr.append(n)
print(sum(arr))