
T=int(input())

na=int(input())
A=list(map(int,input().split()))
nb=int(input())
B=list(map(int,input().split()))
ans=0

adict,bdict={}, {}

for i in range(na):
    t=0
    for j in range(i,na):
        t+=A[j]
        if adict.get(t):
            adict[t]+=1
        else:
            adict[t]=1

for i in range(nb):
    t=0
    for j in range(i,nb):
        t+=B[j]
        if bdict.get(t):
            bdict[t]+=1
        else:
            bdict[t]=1
print(adict,bdict)
for _,i in enumerate(adict):
    if bdict.get(T-i):
        ans+=(adict[i]*bdict[T-i])
            
print(ans)
    
