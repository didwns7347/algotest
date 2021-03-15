n,won=map(int,input().split())
money=[int(input()) for x in range(n)]
dp=[0 for x in range(won+1)]
dp[0]=1
for x in range(n):
    for y in range(money[x],won+1):
        dp[y]=dp[y]+dp[y-money[x]]

print(dp[won])
