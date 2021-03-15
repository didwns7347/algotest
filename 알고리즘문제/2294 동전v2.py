n,k=map(int,input().split())
dp=[100001 for x in range(k+1)]
dp[0]=0
coin=[ int(input()) for x in range(n)]

for x in coin:
    for y in range(1,k+1):
        if y>=x:
            dp[y]=min(dp[y],dp[y-x]+1)
if dp[k]==100001:
    print(-1)
else:
    print(dp[k])
