n= int(input())
rgb=[]
dp=[[0,0,0] for x in range(n)]
start=[[0,0,0] for x in range(n)]
for x in range(n):
    a=list(map(int ,input().split()))
    rgb.append(a)
    if x==0:
        dp[0][0]=rgb[0][0]
        dp[0][1]=rgb[0][1]
        dp[0][2]=rgb[0][2]
        start[0][0]=0
        start[0][1]=1
        start[0][2]=2
  
    elif x==n-1:
        if start[x-1][1]==0 and start[x-1][2]==0:
            dp[x][0]=1000000
        elif start[x-1][2]==0:
            dp[x][0]=dp[x-1][1]+rgb[x][0]
        else:
            dp[x][0]=min(dp[x-1][2]+rgb[x][0],dp[x-1][1]+rgb[x][0])

        if start[x-1][2]==1 and start[x-1][0]==1:
            dp[x][1]=1000000
        elif start[x-1][0]==1:
            dp[x][1]=dp[x-1][2]+rgb[x][1]
        else:
            dp[x][1]=min(dp[x-1][2]+rgb[x][1],dp[x-1][0]+rgb[x][1])

        if start[x-1][1]==2 and start[x-1][0]==2:
            dp[x][2]=1000000
        elif start[x-1][0]==2:
            dp[x][2]=dp[x-1][1]+rgb[x][2]
        else:
            dp[x][2]=min(dp[x-1][0]+rgb[x][2],dp[x-1][1]+rgb[x][2])

    else:
        a=dp[x-1][1]+rgb[x][0]
        b=dp[x-1][2]+rgb[x][0]
        if a<b:
            dp[x][0]=a
            start[x][0]=start[x-1][1]
        else:
            dp[x][0]=b
            start[x][0]=start[x-1][2]
        a=dp[x-1][0]+rgb[x][1]
        b=dp[x-1][2]+rgb[x][1]
        if a<b:
            dp[x][1]=a
            start[x][1]=start[x-1][0]
        else:
            dp[x][1]=b
            start[x][1]=start[x-1][2]
        a=dp[x-1][0]+rgb[x][2]
        b=dp[x-1][1]+rgb[x][2]
        if a<b:
            dp[x][2]=a
            start[x][2]=start[x-1][0]
        else:
            dp[x][2]=b
            start[x][2]=start[x-1][1]

for x in start:
    print(x)
for x in dp:
    print(x)

            
        
        
        
