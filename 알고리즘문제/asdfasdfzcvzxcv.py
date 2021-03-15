import sys
from collections import deque
n,m,v=map(int,input().split())
checkb=[0 for x in range(n+1)]
checkd=[0 for x in range(n+1)]
g=[[] for _ in range(n+1)]
for x in range(m):
    a,b=map(int,sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
for x in g:
    x.sort()
out1=[v]
out2=[v]
checkd[v]=1
checkb[v]=1
def dfs(v):
    checkd[v]=1
    for x in g[v]:
        if checkd[x]==0:
            out1.append(x)
            checkd[x]=1
            dfs(x)
def bfs(v):
    q=deque()
    q.append(v)
    t=1001
    while q:
        t=q.popleft()
        for x in g[t]:
            if checkb[x]==0:
                out2.append(x)
                q.append(x)
                checkb[x]=1
dfs(v)
bfs(v)
for x in out1:
    print(x,end=' ')
print()
for y in out2:
    print(y,end=' ')
