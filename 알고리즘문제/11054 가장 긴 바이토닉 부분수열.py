n=int(input())
nlist=list(map(int,input().split()))
def left(s,f):
    if s==f:
        return 0
    mylist=nlist[s:f]
    dp=[0 for _ in range(len(mylist))]
    mn=[0 for _ in range(len(mylist))]
    dp[0]=1
    mn[0]=mylist[0]
    for x in range(1,len(mylist)):
        mx=0
        for y in range(x-1,-1,-1):
            if mylist[x]>mn[y]:
                mx=max(mx,dp[y])
                    
        dp[x]=mx+1
        mn[x]=mylist[x]
    print(dp,end=" ")
    return max(dp)
    
def right(s,f):
    if s==f:
        return 0

    mylist=nlist[s:f]
    dp=[0 for _ in range(len(mylist))]
    mn=[0 for _ in range(len(mylist))]
    dp[0]=1
    mn[0]=mylist[0]
    for x in range(1,len(mylist)):
        mx=0
        for y in range(x-1,-1,-1):
            if mylist[x]<mn[y]:
                mx=max(mx,dp[y])
                    
        dp[x]=mx+1
        mn[x]=mylist[x]
    print(dp)
    return max(dp)
answer=0
for x in range(n):
    answer=max(answer,left(0,x+1)+right(x,n))
print(answer-1)


