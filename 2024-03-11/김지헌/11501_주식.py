import sys
sys.stdin = open("/Users/positive/Desktop/코테스터디/codingtest/2024-03-11/김지헌/주식.txt","r")

def maxProfit(prices):
    maxProfit = 0
    maxFuturePrice = 0
    

    for price in reversed(prices):
        if price > maxFuturePrice:
            maxFuturePrice = price
        maxProfit += maxFuturePrice - price
    
    return maxProfit


def maxProfit2(prices): # 실패
    offset = 0

    prices[offset:].index(max(prices[offset]))

    

T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    print(maxProfit(prices))



