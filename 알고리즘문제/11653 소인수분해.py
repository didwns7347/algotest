n=int(input())
pn=[1]*(n+1)
pn[0],pn[1]=0,0
pnum=[]
cnt=0
for x in range(2,n+1):
    if pn[x]:
        pnum.append(x)
        for y in range(2,n):
            if x*y>n:
                break
            pn[x*y]=0

while True:
    if n%pnum[cnt]==0:
        print(pnum[cnt])
        n=n//pnum[cnt]
        if n==1:
            break
    else:
        cnt+=1
        if len(pnum)==cnt:
            break
    
