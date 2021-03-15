n,m=map(str,input().split())
m=int(m)
n=list(n)
nums=sorted(n,reverse=True)
def do(nlist):
    tmp=nlist[0]
    idx=0
    for x in range(1,len(nlist)):
        if nlist[x]>tmp:
            tmp=nlist[x]
            idx=x
        elif nlist[x]==tmp and idx!=0:
            tmp=nlist[x]
            idx=x
    if idx==0:
        return [nlist[0]]+do(nlist[1:])
    else:
        nlist[0],nlist[idx]=nlist[idx],nlist[0]
        return nlist
def check(nlist):
    for x in range(len(nlist)-1):
        if nlist[x]==nlist[x+1]:
            return True
    return False

if len(n)==1:
    print(-1)
elif len(n)==2 and n[1]==0:
    print(-1)
else:
    for x in range(m):
        if n==nums:
            if check(n):
                n=n
            else:
                n[-1],n[-2]=n[-2],n[-1]
        else:
            n=do(n)

    for x in n:
        print(x,end='')