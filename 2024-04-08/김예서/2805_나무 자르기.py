import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0 
end = max(tree)
result = 0
while(start <= end):
    mid = (start+end)//2
    total = 0
    # 구한 mid로 나무 자르기
    for height in tree:
        if height > mid:
            total += (height-mid)

    if total >= m:
        # 더 적게 자르기
        result = mid
        start = mid+1
    else:
        # 더 많이 자르기
        end = mid-1

print(result)