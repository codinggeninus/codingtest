import sys
sys.stdin = open("/Users/positive/Desktop/코테스터디/codingtest/2024-03-11/김지헌/주식.txt","r")

def maxProfit(prices):
    maxProfit = 0
    maxFuturePrice = 0
    
    # 뒤에서부터 현재 가격과 미래의 최대 가격과의 차이를 계산
    for price in reversed(prices):
        if price > maxFuturePrice:
            maxFuturePrice = price
        maxProfit += maxFuturePrice - price
    
    return maxProfit


def maxProfit2(prices): # 실패
    if not prices:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price
        max_profit += price - min_price

    return max_profit

    

# 입력 받기
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    # 최대 이익 계산 및 출력
    print(maxProfit(prices))



