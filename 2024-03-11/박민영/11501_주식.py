# 리스트 최대값 인덱스 index() 구하기, 인덱스 도달 시 다시 최대값 계산 -> 시간초과
# 뒤에서부터 for문을 돌면 index() 사용할 필요 X

# 테스트 케이스 T, 날의 수 N, 주가 price
# 날별 최대 이익 profit

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))
    profit = 0
    idx = N-1 # 가격 리스트의 마지막 인덱스 저장
    
    for i in range(N-2, -1, -1):
        # 현재값이 더 작다면 -> 차익 계산
        if price[idx] > price[i]:
            profit += (price[idx] - price[i])
        # 현재값이 더 크거나 같다면 -> idx 갱신
        else:
            idx = i

    print(profit)
