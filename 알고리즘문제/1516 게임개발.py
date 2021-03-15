from sys import stdin
from collections import deque
input = stdin.readline

n=int(input())
idg=[0]*(n+1)
g=[[] for _ in range(n+1)]
time=[0]*(n+1)
dist=[0]*(n+1)
for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    for x in range(0,len(tmp)-1):
        if x==0:
            time[i]=tmp[x]
        if x>0:
            idg[i]+=1
            g[tmp[x]].append(i)

q=deque()
for i in range(1,n+1):
    if idg[i]==0:
        q.append(i)
        dist[i]=time[i]

while q:
    now = q.popleft()
    
    for x in g[now]:
        idg[x]-=1
        if dist[x]<dist[now]+time[x]:
            dist[x]=dist[now]+time[x]
        if idg[x]==0:
            q.append(x)
for x in range(1,n+1):
    print(dist[x])
        
