import sys
input = sys.stdin.readline

'''
    1층 3호
    0층 1호 1명
    0층 2호 2명
    0층 3호 3명 
    1층 1호 1명
    1층 2호 3명
    1층 3호 6명

    2층 3호
    0층 1호 1명
    0층 2호 2명
    0층 3호 3명
    1층 1호 1명
    1층 2호 3명
    1층 3호 6명
    2층 1호 1명
    2층 2호 4명
    2층 3호 10명
'''
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    dp = [[-1 for _ in range(n)] for _ in range(k+1)]

    # 0층 i호 초기화
    for i in range(n):
        dp[0][i] = i+1

    for i in range(1, k+1):
        for j in range(n):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    
    print(dp[k][n-1])