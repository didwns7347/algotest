from sys import stdin
input = stdin.readline
n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    if i==0:
        d.append(a)
        d.append(b)
        
    else:
        d.append(b)
dp=[[0 for _ in range(n)] for _ in range(n)]

for x in range(1,n):
    for y in range(0,n-x):
        if x==1:
            dp[y][y+x]=d[y]*d[y+1]*d[y+2]
            continue
        dp[y][y+x]=float("inf")
        for z in range(y,y+x):
            dp[y][y+x]=min(dp[y][x+y],dp[y][z]+dp[z+1][y+x]+d[y]*d[z+1]*d[y+x+1])

'''for x in dp:
    print(x)'''
print(dp[0][n-1])
        
