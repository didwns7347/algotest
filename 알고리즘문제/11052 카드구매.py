n=int(input())
card=list(map(int,input().split()))
card.insert(0,0)
dp=[0 for x in range(n+1)]
dp[0]=card[0]
dp[1]=card[1]
for x in range(2,n+1):
    for y in range(1,x+1):
        dp[x]=max(dp[x],dp[x-y]+card[y])

print(dp[n])
    
