n=int(input())

dp=[ [0  for _ in range(n)] for _ in range(n)]
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))



for i in range(1,n):
    for x in dp:
        print(x)
    for j in range(0,n-i):
       x=j+i
       dp[j][x]=2**32
       for k in range(j,x):
           dp[j][x]=min(dp[j][x],dp[j][k]+dp[k+1][x]+data[j][0]*data[k][1]*data[x][1])
    print()



        

for x in dp:
    print(x)
