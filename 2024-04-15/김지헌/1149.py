# 집의 수 입력
N = int(input())

# 각 집을 빨강, 초록, 파랑으로 칠하는 비용 입력
cost = [list(map(int, input().split())) for _ in range(N)]

# 다이나믹 프로그래밍을 사용하여 최소 비용 계산
for i in range(1, N):
    # 현재 집을 빨강, 초록, 파랑 중 한 가지 색으로 칠할 때의 최소 비용 계산
    cost[i][0] += min(cost[i - 1][1], cost[i - 1][2])  # 현재 집을 빨강으로 칠할 때의 최소 비용
    cost[i][1] += min(cost[i - 1][0], cost[i - 1][2])  # 현재 집을 초록으로 칠할 때의 최소 비용
    cost[i][2] += min(cost[i - 1][0], cost[i - 1][1])  # 현재 집을 파랑으로 칠할 때의 최소 비용

# 마지막 집을 칠하는 비용 중 최솟값 출력
print(min(cost[N - 1]))
