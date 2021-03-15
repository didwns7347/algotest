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
            heapq.heappush(minh,int(num))
            heapq.heappush(maxh,(-int(num),int(num)))
        if op=="D":
            if not minh:
                continue
            else:
                if num=="1":
                    tmp=heapq.heappop(maxh)
                    mlist=[]
                    for i in range(len(maxh)):
                        mlist.append(heapq.heappop(minh))
                    heapq.heappop(minh)
                    for i in mlist:
                        heapq.heappush(minh,i)

     
                else:
                    tmp=heapq.heappop(minh)
                    mlist=[]
                    for i in range(len(minh)):
                        t=heapq.heappop(maxh)[1]
                        mlist.append(t)
                    heapq.heappop(maxh)
                    for i in mlist:
                        heapq.heappush(maxh,(-i,i))
    if minh:
        print(heapq.heappop(maxh)[1],heapq.heappop(minh))
    else:
        print("EMPTY")
