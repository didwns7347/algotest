num=int(input())
rgb=[list(map(int,input().split())) for y in range(num)]
dp=[[0 for x in range(3)] for y in range(num)]
out=1000*1000+1
for x in range(3):    
    for y in range(3):
        if y==x:
            dp[0][y]=rgb[0][y]
        else:
            dp[0][y]=1000*1000+1
    for i in range(1,num):
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+rgb[i][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+rgb[i][1]
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+rgb[i][2]
    for j in range(3):
        if j==x:
            continue
        else:
            out=min(out,dp[num-1][j])
 
        

print(out)
