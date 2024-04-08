#2805
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start+end)//2
    # print(f'start: {start}, end: {end}, mid: {mid}')

    sum = 0
    for tree in trees:
        if tree>mid:
            sum += tree-mid

    # print(f'sum: {sum}')
    if sum >= M:
        start = mid+1
    else:
        end = mid-1

print(end)