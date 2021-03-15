n=int(input())
a=list(map(int,input().split()))

dp=[0 for x in range(n)]

dp[0]=a[0]
for x in range(1,n):
    for y in range(0,x+1):
        if a[x]>a[y]:
            print(x,a[y])
            dp[x]=dp[x]+a[y]
    print(dp[x])
    dp[x]=max(dp[x],dp[x-1])

for x in dp:
    print(x)
print(dp[n-1])
