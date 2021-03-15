def DP1(bd):
    dp=[[0,0,0,0] for _ in range(n)]
    if bd[0][0]+bd[1][0]<=m:
        dp[0][0]=2
        dp[0][1]=2
        dp[0][2]=1
        dp[0][3]=2
    else:
        dp[0][0],dp[0][2],dp[0][1],dp[0][3]=2,2,2,2
    for i in range(1,n):
        if bd[0][i]+bd[1][i]<=m:
            dp[i][2]=min(dp[i-1][1],dp[i-1][3],dp[i-1][0],dp[i-1][2])+1
        if bd[0][i]+bd[0][i-1]<=m:
            dp[i][0]=min(dp[i-1][1],dp[i-1][3])+1
        if bd[1][i]+bd[1][i-1]<=m:
            dp[i][1]=min(dp[i-1][0],dp[i-1][3])+1
        dp[i][3]=min(dp[i-1][0],dp[i-1][1],dp[i-1][2])+2
        
    
    print(dp)
    return min(dp[n-1])
    
for _ in range(int(input())):
    n,m=map(int,input().split())
    board=[]
    tmp1=list(map(int,input().split()))
    tmp2=list(map(int,input().split()))
    if n==1:
        if tmp1[0]+tmp2[0]<=m:
            print(1)
            continue
        else:
            print(2)
            continue
    ans=float("inf")
    for i in range(2):
        board=[]
        if i==0:
            board.append(tmp1[i:]+tmp1[0:i])
            board.append(tmp2[i:]+tmp2[0:i])
        else:
            board.append(tmp1[n-1:]+tmp1[0:n-1])
            board.append(tmp2[n-1:]+tmp2[0:n-1])
        ans=min(ans,DP1(board))

  
    
    
    print(ans)
    


