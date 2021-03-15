num=int(input())
rgb=[list(map(int,input().split())) for y in range(num)]
dp=[[0 for x in range(3)] for y in range(num)]
start=[[0,0,0] for x in range(num)]
dp[0][0]=rgb[0][0]
dp[0][1]=rgb[0][1]
dp[0][2]=rgb[0][2]
start[0][0]=0
start[0][1]=1
start[0][2]=2

for i in range(1,num):

    if i == num-2:
        if start[i-1][0]==0:
            dp[i+1][0]=min(dp[i-1][0]+rgb[i][1]+rgb[i+1][2],
                           dp[i-1][0]+rgb[i][2]+rgb[i+1][1])
        elif start[i-1][0]==1:
            dp[i+1][0]=min(dp[i-1][0]+rgb[i][1]+rgb[i+1][0],
                           dp[i-1][0]+rgb[i][2]+rgb[i+1][0],
                           dp[i-1][0]+rgb[i][1]+rgb[i+1][2])
        else:
            dp[i+1][0]=min(dp[i-1][0]+rgb[i][1]+rgb[i+1][0],
                           dp[i-1][0]+rgb[i][2]+rgb[i+1][0],
                           dp[i-1][0]+rgb[i][2]+rgb[i+1][1])
        
        if start[i-1][1]==0:
            dp[i+1][1]=min(dp[i-1][1]+rgb[i][0]+rgb[i+1][1],
                            dp[i-1][1]+rgb[i][0]+rgb[i+1][2],
                            dp[i-1][1]+rgb[i][2]+rgb[i+1][1])
        elif start[i-1][1]==1:
            dp[i+1][1]=min(dp[i-1][1]+rgb[i][0]+rgb[i+1][2],
                          dp[i-1][1]+rgb[i][2]+rgb[i+1][0])
        else:
            dp[i+1][1]=min(dp[i-1][1]+rgb[i][0]+rgb[i+1][1],
                            dp[i-1][1]+rgb[i][2]+rgb[i+1][0],
                            dp[i-1][1]+rgb[i][2]+rgb[i+1][1])
        

        if start[i-1][2]==0:
            dp[i+1][2]=min(dp[i-1][2]+rgb[i][0]+min(rgb[i+1][1],rgb[i+1][2]),
                              dp[i-1][2]+rgb[i][1]+rgb[i+1][2])
        elif start[i-1][2]==1:
            dp[i+1][2]=min(dp[i-1][2]+rgb[i][0]+min(rgb[i+1][1],rgb[i+1][2]),
                              dp[i-1][2]+rgb[i][1]+rgb[i+1][2])
        else:
            dp[i+1][2]= min(dp[i-1][2]+rgb[i][0]+rgb[i+1][1],
                            dp[i-1][2]+rgb[i][1]+rgb[i+1][0])
        break
    else:

        if rgb[i][0]+dp[i-1][1]>rgb[i][0]+dp[i-1][2]:
            dp[i][0]=rgb[i][0]+dp[i-1][2]
            start[i][0]=start[i-1][2]
        else:
            dp[i][0]=rgb[i][0]+dp[i-1][1]
            start[i][0]=start[i-1][1]

        if rgb[i][1]+dp[i-1][0]>rgb[i][1]+dp[i-1][2]:
            dp[i][1]=rgb[i][1]+dp[i-1][2]
            start[i][1]=start[i-1][2]
        else:
            dp[i][1]=rgb[i][1]+dp[i-1][0]
            start[i][1]=start[i-1][0]

        if rgb[i][2]+dp[i-1][0]>rgb[i][2]+dp[i-1][1]:
            dp[i][2]=rgb[i][2]+dp[i-1][1]
            start[i][2]=start[i-1][1]
        else:
            dp[i][2]=rgb[i][2]+dp[i-1][0]
            start[i][2]=start[i-1][0]
                                        
                
        

print(min(dp[num-1]))
