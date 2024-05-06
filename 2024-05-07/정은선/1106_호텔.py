# 풀이1 - DFS (시간초과)
import sys
input = sys.stdin.readline

def dfs(cost, person):
    global min_cost
    #만약 고객 수가 목표한 값에 도달하면
    if person >= c:
        #최소 비용 갱신
        min_cost = min(min_cost, cost)
        return
    #모든 정보에 대해 cost, person 추가 후 재귀 함수 실행
    for i in range(n):
        cost += arr[i][0]
        person += arr[i][1]
        print(cost, person)
        dfs(cost, person)
        cost -= arr[i][0]
        person -= arr[i][1]
        
#입력 받기
c, n = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
min_cost = float("inf") #최소비용 초기화

dfs(0, 0)
print(min_cost)

#풀이2 - dp
c, n = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dp = [1e7 for _ in range(c+100)] #dp 테이블 초기화
dp[0] = 0

#비용, 고객 정보에 대하여 해당 고객수까지의 최소 비용 갱신
for a, b in arr:
    for i in range(b, c+100):
        dp[i] = min(dp[i-b]+a, dp[i])

print(min(dp[c:]))