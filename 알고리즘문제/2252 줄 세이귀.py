n,m=map(int,input().split())
g=[[]  for _ in range(n+1)]
indg=[ 0 for _ in range(n+1)]
check=[0 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    indg[b]+=1

from collections import deque
q=deque()
out=[]
for x in range(1,n+1):
    if indg[x]==0:
        q.append(x)
        check[x]=1
while q:
    now = q.popleft()
    print(now,end=" ")
    for x in g[now]:        
        indg[x]-=1
        if indg[x]==0:
            q.append(x)
    

    
    
