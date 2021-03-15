from sys import stdin
from collections import deque
import sys
n=int(input())
g=[[] for _ in range(n+1)]
dist=[0 for _ in range(n+1)]
indegree=[0 for _ in range(n+1)]
time=[0 for _ in range(n+1)]
start=1
for i in range(n):
    tmp=list(map(int,input().split()))
    dist[i+1]=tmp[0]
    indegree[i+1]=tmp[1]
    if tmp[0]>0:
        for x in tmp[2:]:
            g[x].append(i+1)
q=deque()

for x in range(1,n+1):
    if indegree[x]==0:
        q.append(x)
        time[x]=dist[x]


while q:
    now=q.popleft()

    for x in g[now]:
        if time[x]<dist[x]+time[now]:
            time[x]=dist[x]+time[now]
        if indegree[x]-1==0:
            q.append(x)
        indegree[x]-=1
    

print(max(time))
