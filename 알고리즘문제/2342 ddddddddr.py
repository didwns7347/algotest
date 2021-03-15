import sys
work=list(map(int,input().split()))
n=len(work)-1
power=[ [0,2,2,2,2],
        [0,1,3,4,3],
        [0,3,1,3,4],
        [0,4,3,1,3],
        [0,3,4,3,1]]
if n==0:
    print(0)
    sys.exit()
dp=[[[0 for _ in range(n)] for _ in range(5)] for _ in range(5)]
dp[work[0]][0][0]=2
dp[0][work[0]][0]=2
for i in range(1,n):
    for j in range(5):
        for k in range(5):
            if dp[j][k][i-1]!=0:
                if (dp[work[i]][k][i]==0):
                    dp[work[i]][k][i]=power[j][work[i]]+dp[j][k][i-1]
                else:
                    dp[work[i]][k][i]=min(dp[work[i]][k][i], power[j][work[i]]+dp[j][k][i-1])
                if(dp[j][work[i]][i]==0):
                    dp[j][work[i]][i]=power[k][work[i]]+dp[j][k][i-1]
                else:
                    dp[j][work[i]][i]=min(dp[j][work[i]][i], power[k][work[i]]+dp[j][k][i-1])
    
        
                    
                
answer=400001
for i in range(5):
    for j in range(5):
        if dp[i][j][n-1]!=0:
            answer=min(dp[i][j][n-1],answer)
    
print(answer)
