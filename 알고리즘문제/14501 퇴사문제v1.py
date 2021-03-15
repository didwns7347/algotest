n=int(input())
work=[list(map(int,input().split())) for x in range(n)]

dp=[0 for x in range(n)]
dp[0]=work[0][1]
out=0
for x in range(1,n):
    if work[x][0]+x>n:
        dp[x]=0
    else:
        t=0
        for y in range(x-1,-1,-1):
            if work[y][0]+y<=x:
                t=max(dp[y],t)                
                
        dp[x]+=work[x][1]+t
        
        out=max(out,dp[x])
    

print(out)
