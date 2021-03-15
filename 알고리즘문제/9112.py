import sys
n=int(input())
dp=[0 for x in range(n)]
k=list(map(int,input().split()))

dp[0]=k[0]
tmp=0
for x in range(1,n):
    if dp[x-1]>=0:
        tmp=dp[x-1]+k[x]
    else:
        tmp=k[x]
    if tmp<0:
        dp[x]=k[x]
    else:
        dp[x]=dp[x]+tmp


print(max(dp[0:n]))
            
