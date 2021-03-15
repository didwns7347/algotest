n=int(input())
dp=[0]*100001
sum=2
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    if sum*sum==i:
        dp[i]=1
        sum+=1
print(dp[n])
