n,k=map(int,input().split())
bag=[]
for i in range(n):
    bag.append(list(map(int,input().split())))
dp=[[0]*(k+1)for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j>= bag[i-1][0]:
            dp[i][j]=max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][k])