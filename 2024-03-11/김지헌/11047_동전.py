import sys
sys.stdin = open("/Users/positive/Desktop/코테스터디/codingtest/2024-03-11/김지헌/동전.txt","r")

N,M = map(int,input().split())

coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

count = 0
while(True):
    N = N-1
    coin_count = M // coins[N]
    if(coin_count == 0):
        continue
    else:
        count += coin_count
        M = M%coins[N]
    if(M==0):
        break
    if(N==-1):
        break

print(count)
