# 이진탐색, 실버2
# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

start = 0
end = max(n_list)
height = 0

while (start <= end):
    total = 0
    # 이진탐색 시작
    mid = (start + end) // 2
    for x in n_list:
        if x > mid:
            total += x - mid
    # 원하는 길이보다 적은 경우
    if total < m:
        end = mid - 1
    else:
        height = mid
        # 최대한 적게 자르는게 목표
        start = mid + 1
        
print(height)