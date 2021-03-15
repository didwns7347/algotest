#트리순회 2263
#인오더 = left root right
#포스트= left right root
import sys
sys.setrecursionlimit(10**8)
n=int(input())
iod=list(map(int,input().split()))
pod=list(map(int,input().split()))
search=[0 for _ in range(n+1)]
out=[]
for x in range(n):
    search[iod[x]]=x
def maketreev2(ios,iof,pos,pof):
    if pos<=pof:
        out.append(pod[pof])
        root=search[pod[pof]]
        lcnt=root-ios
        rcnt=iof-root
        maketreev2(ios,ios+lcnt-1,pos,pos+lcnt-1)
        maketreev2(iof-rcnt+1,iof,pof-rcnt,pof-1)
        
maketreev2(0,n-1,0,n-1)
            
            
for x in out:
    print(x,end=" ")
    
