import sys
n=int(input())
nlist=[0 for x in range(10001)]
for x in range(n):
    tmp=int(sys.stdin.readline().strip())
    nlist[tmp]+=1

for x in range(1,len(nlist)):
    if nlist[x]!=0:
        for y in range(nlist[x]):
            print(x)
        
