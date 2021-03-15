n,m=map(int,input().split())

dp=[[0 for x in range(n)] for y in range(m)]

for x in range(m):
    for y in range(n):
        if x==0:
            dp[x][y]=y
        elif y==0:
            dp[x][y]=x
        else:
            dp[x][y]=dp[x][y-1]+dp[x][0]+1
print(dp[m-1][n-1])
    
