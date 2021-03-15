from sys import stdin
from collections import deque
input=stdin.readline
def solve(f,idg,g,time):
    q=deque()
    dist=[0 for _ in range(n+1)]
    for x in range(1,n+1):
        if idg[x]==0:
            q.append(x)
            dist[x]=time[x-1]
  
    while q:
        now = q.popleft()
        for x in g[now]:
            idg[x]-=1
            if dist[x]<dist[now]+time[x-1]:
                dist[x]=dist[now]+time[x-1]
            if idg[x]==0:
                q.append(x)
    return dist[f]
                
        

for _ in range(int(input())):
    n,k=map(int,input().split())
    time=list(map(int , input().split()))
    g=[[] for _ in range(n+1)]
    idg=[0 for _ in range(n+1)]
    for _ in range(k):
        a,b=map(int,input().split())
        g[a].append(b)
        idg[b]+=1
    win=int(input())
    print(solve(win,idg,g,time))
    
        
    
