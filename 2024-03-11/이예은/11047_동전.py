# 그리디, 실버4
# https://www.acmicpc.net/problem/11047

# 동전 종류, 합
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
cnt = 0

coins.sort(reverse=True)

for coin in coins:
    if k <= 0:
        break
    if coin > k:
        continue
    cnt += k // coin
    # 나누고 남은 금액 할당
    k %= coin

print(cnt)
