n=int(input())
g=[list(map(int,input().split())) for _ in range(n)]
cost=[[ float("inf") for _ in range(2**n)] for _ in range(n)]

def DFS(now,ck,co):
    w=0
    for x in range(n):
        w+=(2**x)*ck[x]
    if w==2**n:
        return
    cost[now][w]=min(co,cost[now][w])
    for x in range(n):
        if ck[x]==0 and g[now][x]!=0:
            ck[x]=1
            DFS(x,ck,co+g[now][x])
            ck[x]=0

check=[0]*n            
check[0]=1
DFS(0,check,0)
ans=float("inf")
node=0
for x in range(n):
    if ans>cost[x][-1]:
        ans=cost[x][-1]
        node=x
print(ans+g[node][0])
    
