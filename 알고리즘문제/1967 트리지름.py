import heapq
from collections import deque
n=int(input())
board=[[] for _ in range(n+1)]

MAX=10000*100000000
def init():
    for _ in range(n-1):
        a,b,c=map(int,input().split())
        board[b].append([c,a])
        board[a].append([c,b])

    
def dijkstra(start,target=-1):
    q=deque()
    dist=[MAX for _ in range(n+1)]
    check=[0 for _ in range(n+1)]
    q.append(start)
    dist[start]=0
    check[start]=1
    while q:
        node=q.popleft()
        if node==target:
            return dist[node],0
        for ncost,nnode in board[node]:
            if check[nnode]==0:
                check[nnode]=1
                q.append(nnode)
                dist[nnode]=min(dist[nnode],dist[node]+ncost)
    answer=0
    for x in range(1,n+1):
        if check[x]==0:
            continue
        answer=max(answer,dist[x])
    return answer,dist.index(answer)
init()
out=0

d1,a=dijkstra(1)
d2,b=dijkstra(a)
c,d=dijkstra(a,b)
print(c)
