n = int(input())  # 계단의 개수 입력
stairs = [0] * (n + 1)  # 각 계단에 쓰여 있는 점수를 저장할 리스트
dp = [0] * (n + 1)  # 각 계단까지의 최대 점수를 저장할 리스트

# 각 계단에 쓰여 있는 점수 입력
for i in range(1, n + 1):
    stairs[i] = int(input())

# 첫 번째 계단과 두 번째 계단까지의 최대 점수 초기화
dp[1] = stairs[1]
if n > 1:
    dp[2] = stairs[1] + stairs[2]

# 다이나믹 프로그래밍을 사용하여 각 계단까지의 최대 점수 계산
for i in range(3, n + 1):
    # 현재 계단을 밟는 경우와 이전 계단을 밟고 현재 계단을 밟는 경우 중 더 큰 값을 선택하여 최대 점수를 갱신
    dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]

# 마지막 계단까지의 최대 점수 출력
print(dp[n])
