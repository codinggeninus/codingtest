import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
# 동전의 가치 입력 받기
for i in range(n):
    coins.append(int(input()))

# 내림차순 정렬
coins.sort(reverse=True)

# 필요한 동전의 개수
cnt = 0
# k가 0이 아니라면 반복
while(k != 0):    
    # 나머지가 0이하면 건너뛰기
    for coin in coins:
        if k % coin < 0:
            continue
        # k를 coin으로 나눈 몫을 cnt에 누적
        cnt += k//coin
        k%=coin

print(cnt)


