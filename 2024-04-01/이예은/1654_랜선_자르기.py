# 이진탐색, 실버 2
# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]

# 주어진 랜선 길이가 모두0인 경우 zeroDivionError 발생
start = 1
end = max(k_list)

while (start <= end):
    cnt = 0
    mid = (start + end) // 2
    for x in k_list:
        cnt += x // mid

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
