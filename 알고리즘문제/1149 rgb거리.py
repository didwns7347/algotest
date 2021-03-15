num=int(input())
rgb=[list(map(int,input().split())) for y in range(num)]

dp=[[0 for x in range(3)] for y in range(num)]
dp[0][0]=rgb[0][0]
dp[0][1]=rgb[0][1]
dp[0][2]=rgb[0][2]
for i in range(1,num):
    dp[i][0]=min(rgb[i][0]+dp[i-1][1],rgb[i][0]+dp[i-1][2])
    dp[i][1]=min(rgb[i][1]+dp[i-1][0],rgb[i][1]+dp[i-1][2])
    dp[i][2]=min(rgb[i][2]+dp[i-1][0],rgb[i][2]+dp[i-1][1])
    
print(min(dp[num-1]))
