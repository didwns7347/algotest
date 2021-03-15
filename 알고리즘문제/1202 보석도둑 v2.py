from sys import stdin
import heapq
input=stdin.readline
answer=0
n,k = map(int,input().split())
info=[[] for _ in range(1000001)]
for x in range(n):
    w,v = map(int,input().split())
    heapq.heappush(info[w],-v)
bag=[]
for _ in range(k):
    c=int(input())
    heapq.heappush(bag,c)
heap=[]
tmp=0
while bag:
    b=heapq.heappop(bag)
    for x in range(tmp,b+1):
        if info[x]:
            while info[x]:
                  heapq.heappush(heap,heapq.heappop(info[x]))
    if not heap:#가방에 해당하는 무게의 보석이 없는경우 가방에 담지않고 넘
        continue
    answer+=-heapq.heappop(heap)
    tmp=b       
        
print(answer)
