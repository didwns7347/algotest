from sys import stdin
import heapq

input=stdin.readline
n,m=map(int,input().split())
dist=[float('inf') for _ in range(n+1)]

board=[[] for _ in range(n+1)]
start=int(input())
for _ in range(m):
    a,b,c=map(int,input().split())
    board[a].append([b,c])


q=[]
heapq.heappush(q,[0,start])
dist[start]=0

while q:
    cost,nxt=heapq.heappop(q)
    for nnxt,cst in board[nxt]:
        ncost=cost+cst
        if dist[nnxt]>ncost: 
            dist[nnxt]=ncost
            heapq.heappush(q,[ncost,nnxt])
    

for x in range(1,n+1):
    if dist[x]>10000000000:
        print("INF")
    else :
        print(dist[x])
    
