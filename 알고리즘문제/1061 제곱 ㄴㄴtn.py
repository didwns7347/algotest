import math
mini,maxi=map(int,input().split())
pn=[ 1 for _ in range(1000001)]
pn[0]=0
pn[1]=0
scope=int(math.sqrt(maxi))
jj=[x*x for x in range(2,scope+1)]

answer=0
ck=[ 1 for _ in range(maxi-mini+1)]
for r in jj:
    cidx=math.ceil(mini/r)*r-mini
    while cidx <= maxi - mini:
        ck[cidx]=0
        cidx+=r

    
        
        
print(sum(ck))

                        

        
    
