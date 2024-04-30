# 크기가 2×n인 직사각형을 채우는 방법의 수를 저장할 리스트
# dp[i]는 크기가 2×i인 직사각형을 채우는 방법의 수를 의미함
dp = [0] * 1001

# 초기값 설정
dp[1] = 1
dp[2] = 2

# 다이나믹 프로그래밍을 사용하여 크기가 2×n인 직사각형을 채우는 방법의 수 계산
def fill_rectangle(n):
    for i in range(3, n + 1):
        # dp[i] = dp[i-1] + dp[i-2]
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

# 입력 받기
n = int(input())

# 직사각형 채우는 방법의 수 계산
fill_rectangle(n)

# 결과 출력
print(dp[n])
