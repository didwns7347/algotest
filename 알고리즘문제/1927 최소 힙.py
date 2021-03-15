import heapq
import sys
heap=[]
n=int(input())

for x in range(n):
    num=int(sys.stdin.readline().strip())
    if num>0:
        heapq.heappush(heap,num)
    if num==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
