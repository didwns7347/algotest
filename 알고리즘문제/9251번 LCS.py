a=list(input())
b=list(input())
stra=[0]
strb=[0]

for x in a:
    stra.append(x)
for x in b:
    strb.append(x)
dp=[[0 for _ in range(len(stra))] for _  in range(len(strb))]
for x in range(1,len(strb)):
    for y in range(1,len(stra)):
        if strb[x]==stra[y]:
            dp[x][y]=dp[x-1][y-1]+1
        else:
            dp[x][y]=max(dp[x-1][y],dp[x][y-1])
print(dp[-1][-1])
            
