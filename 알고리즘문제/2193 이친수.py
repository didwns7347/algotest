n=int(input())
dp=[[0 for x in range(n)],[0 for x in range(n)]]

dp[0][0]=0
dp[1][0]=1

for x in range(1,n):
    dp[1][x]=dp[1][x]+dp[0][x-1]
    dp[0][x]=dp[0][x]+dp[0][x-1]
    dp[0][x]=dp[0][x]+dp[1][x-1]


print(dp[0][n-1]+dp[1][n-1])
