from sys import stdin
import heapq
input=stdin.readline

N=int(input())
M=int(input())

g=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c= map(int,input().split())
    g[a].append([b,c])

start , fin = map(int, input().split())

dist=[ float("inf") for _ in range(N+1)]
heap=[]
dist[start]=0
answer=[[] for _ in range(N+1)]
heapq.heappush(heap,[0,start])
while heap:
    cost,node=heapq.heappop(heap)
    for nxt,c in g[node]:
        if dist[nxt]>dist[node]+c:
            dist[nxt]=dist[node]+c
            answer[nxt]=answer[node]+[nxt]
            heapq.heappush(heap,[dist[nxt],nxt])

print(dist[fin])
print(len(answer[fin])+1)
print(start , end=" ")
for x in answer[fin]:
    print(x,end=" ")
