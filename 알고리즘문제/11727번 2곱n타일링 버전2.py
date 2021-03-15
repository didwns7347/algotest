n=int(input())
dp=[0 for x in range(n)]
dp[0]=1
if n>1:
    dp[1]=3

for x in range(2,n):
    dp[x]=dp[x-1]+2*dp[x-2]
print(dp[n-1]%10007)
