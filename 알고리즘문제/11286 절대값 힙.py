import heapq
import sys
numdict={}
heap=[]
for _ in range(int(input())):
    op=int(sys.stdin.readline())
    if op!=0:
        if op in numdict:
            numdict[op]+=1
        else:
            numdict[op]=1
        heapq.heappush(heap,abs(op))
    else:
        if not heap:
            print(0)
        else:
            tmp=heapq.heappop(heap)
            mtmp=tmp*-1
            if mtmp in numdict and numdict[mtmp]>0:
                print(mtmp)
                numdict[mtmp]-=1
            else:
                print(tmp)
                numdict[tmp]-=1
        
        
