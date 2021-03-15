n=int(input())
work=[list(map(int,input().split())) for x in range(n)]

dp=[0 for x in range(n)]
dp[0]=work[0][1]
for x in range(1,n):
    if x+work[x][0]>n-1:
        dp[x]=dp[x-1]

    elif x<work[x-1][0]+x-1:
        tmp=-1
        for y in range(x-1,-1,-1):
            if work[y][0]+y<=x:
                tmp=y
                break
        if tmp==-1:
            print(tmp)
            dp[x]=max(dp[x-1],work[x][1])
        else:
            print(tmp)
            dp[x]=max(dp[x-1],work[x][1]+dp[tmp])
    else:
        dp[x]=dp[x-1]+work[x][1]
print(dp)
print(dp[n-1])
