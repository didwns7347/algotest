from sys import stdin
import heapq
input=stdin.readline
MAX=10000*1000
N,M,X=map(int,input().split())
g=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    g[a].append([b,c])
    
dist=[[ MAX for _ in range(N+1)] for _ in range(N+1)]
for x in range(1,N+1):
    heap=[]
    dist[x][x]=0
    heapq.heappush(heap,[0,x])
    while heap:
        cost,node=heapq.heappop(heap)
        for nxt,c in g[node]:
            if dist[x][nxt]>dist[x][node]+c:
                dist[x][nxt]=dist[x][node]+c
                heapq.heappush(heap,[dist[x][nxt],nxt])
answer=0

for x in range(1,N+1):
    answer=max(answer,dist[x][X]+dist[X][x])
print(answer)
