n=int(input())
nums=[0]
num=list(map(int,input().split()))
for x in num:
    nums.append(x)
dp=[0 for _ in range(n+1)]
maxi=0

for x in range(1,n+1):
    mini=0
    for y in range(0,x):
        if nums[x]>nums[y]:
            if mini < dp[y]:
                mini=dp[y]
        dp[x]=mini +1
        if maxi < dp[x]:
            maxi = dp[x]
print(maxi)

    
