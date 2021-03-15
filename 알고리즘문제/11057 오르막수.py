n=int(input())
dp=[[0 for x in range(10)] for y in range(n)]

dp[0]=[1,1,1,1,1,1,1,1,1,1]

for x in range(1,n):
    for y in range(10):
        for z in range(y,10):
            dp[x][z]=dp[x][z]+dp[x-1][y]

print(sum(dp[n-1])%10007)
