#1644 소수의 연속합
n=int(input())
pnum=[]
ans=0
pn=[1]*(n+1)
pn[0],pn[1]=0,0
for i in range(2,n//2):
    if pn[i]!=0:
        for j in range(2,n):
            if i*j>n:
                break
            pn[i*j]=0
for x in range(1,n+1):
    if pn[x]==1:
       pnum.append(x)



s,f=0,0

while True:

    if f==len(pnum) and s==len(pnum):
        break
    if sum(pnum[s:f])==n:
        ans+=1
        if f<len(pnum):
            f+=1
        else:
            s+=1
    elif sum(pnum[s:f])<n:
        if f<len(pnum):
            f+=1
        else:
            s+=1
    else:
        s+=1
               
print(ans)
