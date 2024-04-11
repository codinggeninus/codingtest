N, M = map(int, input().split())
array = list(map(int, input().split()))
start = 1
end = max(array)
while start <= end:
    count = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            count += x - mid

    if count >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
