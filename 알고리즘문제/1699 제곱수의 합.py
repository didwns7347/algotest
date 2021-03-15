n=int(input())
dp=[100000 for x in range(n+1)]

for x in range(1,n):
    if x*x>n:
        break
    dp[x*x]=1


for x in range(1,n+1):
    for y in range(1,int(x/2)):

        if y*y>x:
            break
        dp[x]=min(dp[x-y*y]+1,dp[x])

print(dp[n])
