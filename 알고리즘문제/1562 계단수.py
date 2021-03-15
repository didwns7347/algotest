import sys
n=int(input())
dp=[[[0 for _ in range(1024)] for _ in range(10)]for _ in range(n+1)]
limit=1000000000
ans=0
for x in range(1,10):
    dp[1][x][1<<x]=1
    
for x in range(2,n+1):
    for y in range(0,10):
        for z in range(0,1024):
            if y==0:
                dp[x][0][z|(1<<0)]=(dp[x][0][z|(1<<0)]+dp[x-1][1][z])%limit
            elif y==9:
                dp[x][9][z|(1<<9)]=(dp[x][9][z|(1<<9)]+dp[x-1][8][z])%limit
            else:
                dp[x][y][z|(1<<y)]=(dp[x][y][z|(1<<y)]+dp[x-1][y-1][z])%limit
                dp[x][y][z|(1<<y)]=(dp[x][y][z|(1<<y)]+dp[x-1][y+1][z])%limit
for x in range(10):
    ans=(ans+dp[n][x][1023])%limit

print(ans)


                
                                    
        
