from collections import deque
q=deque()
n=int(input())
tree=[[] for x in range(n+1)]
par=[0 for x in range(n+1)]
for x in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
for x in tree[1]:
    q.append([1,x])

while True:
    if not q:
        break
    tmp=q.popleft()
    nx=tmp[0]
    ny=tmp[1]
    par[ny]=nx
    for i in tree[ny]:
        if par[i]==0 :
            q.append([ny,i])
for x in range(2,n+1):
    print(par[x])
