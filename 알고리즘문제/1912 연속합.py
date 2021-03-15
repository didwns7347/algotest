n=int(input())
a=list(map(int,input().split()))
tmp=0
maxn=0
cnt=0
m=-1000
for x in range(n):
    if a[x]>=0:
        cnt+=1
        tmp=a[x]+tmp
    else:
        m=max(m,a[x])
        tmp=0
    maxn=max(maxn,tmp)

if cnt==0:
    print(m)
else:
    print(maxn)


