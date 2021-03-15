n=int(input())
t=[list(map(int,input().split()))for x in range(n)]
dp=[[0 for x in range(n)]for y in range(n)]
dp[0][0]=t[0][0]


for x in range(1,n):
    for y in range(x+1):

        if y==0:
            dp[x][y]=dp[x-1][y]+t[x][y]
        elif y==x:
            dp[x][y]=dp[x-1][y-1]+t[x][y]
            
        else:
            dp[x][y]=max(dp[x-1][y],dp[x-1][y-1])+t[x][y]
        
            
print(max(dp[n-1]))
