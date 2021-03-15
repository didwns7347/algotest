import heapq
import sys
n=int(input())

for x in range(n):
    minh=[]
    maxh=[]
    delmin=[]
    delmax=[]
    m=int(input())
    for x in range(m):
        op,num=map(str,sys.stdin.readline().split())
        
        if op=="I":
            heapq.heappush(minh,int(num))
            heapq.heappush(maxh,(-int(num),int(num)))
        if op=="D":
            if not minh :
                continue
            else:
                if num=="1":
                    delmax.append(heapq.heappop(maxh)[1])
                         
                else:
                    delmin.append(heapq.heappop(minh))
        print(op,num,minh,maxh)
    #print(maxh,minh)
    #print(delmax,delmin)
    
    
    if maxh:
        while True:
            tmp=heapq.heappop(maxh)[1]
            if tmp not in delmin:
                print(tmp,end=" ")
                break
            if not maxh:
                break
        
    if minh:
        while True:
            tmp=heapq.heappop(minh)
            if tmp not in delmax:
                print(tmp)
                break
            if not minh:
                break
                
        
    else:
        print("EMPTY")
