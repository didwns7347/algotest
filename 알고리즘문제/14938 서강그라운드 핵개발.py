import heapq
n,m,r=map(int,input().split())
item=list(map(int,input().split()))
road=[[] for _ in range(n+1)]
for _ in range(r):
    a,b,c=map(int,input().split())
    road[a].append([b,c])
    road[b].append([a,c])
def dijk(start):
    heap=[]
    answer=0
    dist=[float("inf") for _ in range(n+1)]
    dist[start]=0
    heapq.heappush(heap,[0,start])
    while heap:
        cost,node=heapq.heappop(heap)
        for nxt,nc in road[node]:
            if dist[nxt]>dist[node]+nc:
                dist[nxt]=dist[node]+nc
                heapq.heappush(heappush[dist[nxt],nxt])
    for x in range(1,n+1):
        if dist[x]<=m:
            answer+=item[x-1]
    return answer
out=0
for x in range(1,n+1):
    out=max(out,dijk(x))
print(out)
