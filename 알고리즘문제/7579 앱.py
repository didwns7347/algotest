n,m=map(int,input().split())
memo=[0]+list(map(int,input().split()))
cost=[0]+list(map(int,input().split()))
dp=[[0 for _ in range(sum(cost)+1)] for _ in range(n+1)]
result=sum(cost)

for i in range(1,n+1):
    M=memo[i]
    c=cost[i]

    for j in range(1,sum(cost)+1):
        if j<c:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(M+dp[i-1][j-c],dp[i-1][j])
        if dp[i][j]>= m:
            result=min(result,j)
for x in dp:
    print(x)
if m!=0:
    print(result)
else:
    print(0)
        
