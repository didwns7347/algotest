cnt=int(input())
while cnt>0:
    n,m=map(int,input().split())
    dp=[[0 for x in range(n)] for y in range(m)]

    for x in range(m):
        for y in range(0,n):
            if y>x:
                break
            elif y==0:
                dp[x][y]=x+1
            elif y==x:
                dp[x][y]=1
            else:
                dp[x][y]=dp[x-1][y-1]+dp[x-1][y]
    print(dp[m-1][n-1])
    cnt-=1

