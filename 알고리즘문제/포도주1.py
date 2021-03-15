import sys
n = int(input())
dp=[0 for x in range(n)]
wine=[0]*n

for x in range(n):

    wine[x]=int(sys.stdin.readline().strip())
    if x==0:
        dp[x]=wine[x]

    elif x==1:
        dp[x]=wine[x]+dp[x-1]

    elif x==2:
        dp[x]=max(wine[x-2]+wine[x],wine[x-1]+wine[x],wine[x-2]+wine[x-1])
    else:
        dp[x]=max(dp[x-3]+wine[x]+wine[x-1],dp[x-2]+wine[x])
        dp[x]=max(dp[x],dp[x-1])

print(dp[n-1])
