from sys import stdin
import heapq
input=stdin.readline
MAX=float("inf")
N,E=map(int,input().split())
g=[[] for _ in range(N+1)]
for x in range(E):
    a,b,c=map(int,input().split())
    g[a].append([b,c])
    g[b].append([a,c])
d1,d2=map(int,input().split())


def DI(start,destination):
    heap=[]
    dist=[ MAX for _ in range(N+1)]
    dist[start]=0
           
    heapq.heappush(heap,[0,start])
    while heap:
        cost,nxt=heapq.heappop(heap)
        
        for nn,cst in g[nxt]:
            if dist[nn]>dist[nxt]+cst:
                dist[nn]=dist[nxt]+cst
                heapq.heappush(heap,[dist[nn],nn])
    #print(dist)
    return dist[destination]

a=DI(1,d1)+DI(d1,d2)+DI(d2,N)
b=DI(1,d2)+DI(d2,d1)+DI(d1,N)
answer=min(a,b)
if answer>100000000000000000000:
    print(-1)
else:
    print(answer)
