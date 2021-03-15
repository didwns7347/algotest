from collections import deque
N,S,D,F,B,K= map(int,input().split())
check=[False for x in range(N+1)]
if K:
    police=list(map(int,input().split()))
    for x in police:
        check[x]=True
else:
    police=[]

d=[-1 for x in range(N+1)]
q=deque()
check[S]=True
d[S]=0
q.append(S)
ans=-1
while q:
    tmp=q.popleft()
    if tmp==D:
        ans=d[tmp]
        break
    if tmp+F<=N  and tmp+F>=1 and check[tmp+F]==False:
        check[tmp+F]=True
        q.append(tmp+F)
        d[tmp+F]=d[tmp]+1

    if tmp-B>=1 and tmp-B<=N and  check[tmp-B]==False:
        check[tmp-B]=True
        q.append(tmp-B)
        d[tmp-B]=d[tmp]+1


if ans==-1:
    print("BUG FOUND")
else:
    print(ans)

