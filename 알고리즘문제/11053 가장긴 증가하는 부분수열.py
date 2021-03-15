n=int(input())
nums=list(map(int,input().split()))

dp=[0 for x in range(n+1)]
mnum=[0 for x in range(n+1)]
dp[0]=1
mnum[0]=nums[0]
for i in range(1,n):
    mx=0
    for j in range(i-1,-1,-1):
        if nums[i]>mnum[j]:
            mx=max(mx,dp[j])
    dp[i]=mx+1
    mnum[i]=nums[i]

print(max(dp))
