n=int(input())
dp=[0 for x in range(n)]
dp[0]=1
dp[1]=2
if n<2:
    print(dp[n-1])
else:    
    for x in range(2,n):
        tmp=dp[x-1]+dp[x-2]
        dp[x]=tmp%10007
    print(dp[n-1])
