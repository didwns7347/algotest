import heapq
from collections import deque
n=int(input())
board=[[] for _ in range(n+1)]

MAX=10000*10000000
def init():
    for _ in range(n):
        tmp = list(map(int,input().split()))
        v=tmp[0]
        q=deque(tmp[1:len(tmp)-1])
        while q:
            a=q.popleft()
            b=q.popleft()
            board[v].append([b,a])
def dijkstra(start,target=-1):
    heap=[]
    dist=[MAX for _ in range(n+1)]
    check=[0 for _ in range(n+1)]
    heapq.heappush(heap,[0,start])
    dist[start]=0
    check[start]=1
    while heap:
        cost,node=heapq.heappop(heap)
        if node==target:
            return dist[node],0
        for ncost,nnode in board[node]:
            if dist[nnode]>dist[node]+ncost:
                dist[nnode]=dist[node]+ncost
                heapq.heappush(heap,[dist[nnode],nnode])
               
    #print(dist)
    answer=0
    for x in range(1,n+1):
        if dist[x]!=MAX:
            answer=max(answer,dist[x])
    return answer,dist.index(answer)

    
    
init()
out=0

d1,a=dijkstra(1)

d2,b=dijkstra(a)
c,d=dijkstra(a,b)
print(c)
