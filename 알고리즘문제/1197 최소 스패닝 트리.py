from sys import stdin
import heapq
import sys
input = stdin.readline

answer=0
v,e= map(int,input().split())
if v==1:
    print(0)
    sys.exit()

    
heap=[]
for _ in range(e):
    a,b,c=map(int,input().split())
    heapq.heappush(heap,[c,a,b])
parent=[ x for x in range(v+1)]

def union(a,b):
    a=find(a)
    b=find(b)
    parent[b]=a
def find(a):
    if a==parent[a]:
        return a
    tmp=find(parent[a])
    parent[a]=tmp
    return tmp

cost,ta,tb=heapq.heappop(heap)
answer+=cost
union(ta,tb)

boss=ta
fin=False
if not heap:
    print(answer)
    sys.exit()
mycost=cost
while heap:
    cost,a,b=heapq.heappop(heap)
    
    if find(a) != find(b):
        answer+=cost
        mycost=max(mycost,cost)
        if find(a)!=boss and find(b)!=boss:
            union(a,b)
            
        elif find(a)==boss:
            union(a,b)
            
        elif find(b)==boss:
            union(b,a)
            
 
    for x in range(1,v+1):
        if find(parent[x])!=boss:
            fin=False
            break
        fin=True
    if fin:
        print(answer-mycost)
        break
    


