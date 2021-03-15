from sys import stdin
import heapq
input=stdin.readline

n,k=map(int,input().split())
answer=0
sdict={}
for x in range(n):
    a,b=map(int,input().split())
    if a not in sdict:
        heap=[]
        sdict[a]=heapq.heappush(heap,-b)
    else:
        heapq.heappush(sdict[a],-b)
for _ in range(k):
    bag=int(input())
    while True:
        if bag in sdict and sdict[bag]:
            break
        bag-=1
    answer+=-1*heapq.heappop(sdict[bag])
    
        
    
