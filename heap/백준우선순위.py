import heapq
import sys
n=int(input())

for x in range(n):
    minh=[]
    maxh=[]
    m=int(input())
    for x in range(m):
        op,num=map(str,sys.stdin.readline().split())
        if op=="I":
            heapq.heappush(minh,int(n))
            heapq.heappush(maxh,(-int(n),int(n)))
        if op=="D":
            if not minh:
                continue
            else:
                if num=="1":
                    tmp=heapq.heappop(maxh)
                    mlist=[]
                    for x in range(len(maxh)):
                        mlist.append(heapq.heappop(minh))
                    heapq.heappop(minh)
                    for x in mlist:
                        heapq.heappush(x)

     
                else:
                    tmp=heapq.heappop(minh)
                    mlist=[]
                    for x in range(len(maxh)):
                        mlist.append(heapq.heappop(maxh)[1])
                    heapq.heappop(maxh)
                    for x in mlist:
                        heapq.heappush(x)
    if q:
        print(heapq.heappop(minh), heapq.heappop(maxh)[1])
    else:
        print("EMPTY")