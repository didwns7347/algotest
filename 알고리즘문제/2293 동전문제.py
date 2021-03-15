n,won=map(int,input().split())
money=[int(input()) for x in range(n)]

dp=[[0 for x in range(won+1)] for y in range(n+1)]
dp[0][0]=1
for x in range(1,n+1):
    for y in range(won+1):
        if y<money[x-1]:
            dp[x][y]=dp[x-1][y]
        elif y==money[x-1]:
            dp[x][y]=dp[x-1][y]+1
        else:
            dp[x][y]=dp[x-1][y]+dp[x][y-money[x-1]]

print(dp[n][won])
