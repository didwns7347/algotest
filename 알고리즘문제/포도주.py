n=int(input())

dp=[[0,0,0] for x in range(n)]
wine=[0 for x in range(n)]
for x in range(0,n):
    wine[x]=int(input())
    if x==0:
        dp[x][0]+=wine[x]
        dp[x][1]+=wine[x]
        dp[x][2]+=wine[x]
    elif x==1:
        dp[x][0]+=wine[x]+wine[x-1]
        dp[x][1]+=wine[x]+wine[x-1]
        dp[x][2]+=wine[x]+wine[x-1]
    elif x==2:
        dp[x][0]= dp[x-1][0]
        dp[x][1]= wine[x] + wine[x - 2]
        dp[x][2]= wine[x] + wine[x - 1]
    else:
        dp[x][0]=dp[x-1][2]
        dp[x][1]=dp[x-1][0]+wine[x]
        dp[x][2]=dp[x-1][1]+wine[x]
    print(dp[x])

print(max(dp[n-1]))
