T = int(input())
sum = 0
for i in range(T):
    k = int(input())
    n = int(input())

    dp=[m for m in range(1,n+1)]
    for i in range(1,k+1):
        for j in range(1,n):
            dp[j]+=dp[j-1]
    print(dp[n-1])

# dp[4]=dp[0]
# dp[5]=dp[0]+dp[1]
# dp[6]=dp[0]+dp[1]+dp[2]

"""
1층은 기본적은 123
담층은 아래층에 앞의 방을 모두 더한값으로
dp상에서 앞의 것을 더하는 규칙과 같아서.. 그렇게했나봄

"""
