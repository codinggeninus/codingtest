# 동전 N종류, 만들어야 하는 동전 가치합 K, 동전의 가치 coin
# 필요한 동전 개수의 최소값 cnt

import sys

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)] # 동전 N종류 가치 오름차순
coin.sort(reverse = True)
cnt = 0

for i in coin:
    # 정지조건
    if K == 0:
        break
    cnt += K // i # 동전 개수 카운트
    K %= i # 동전 가치합 업데이트

print(cnt)